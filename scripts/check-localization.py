#!/usr/bin/env python3
"""Verifica il registro di localizzazione IT/UE contro l'albero delle skill.

Sostituisce, nell'edizione EU/IT, il controllo US-English dell'upstream (D-IT2). Quello garantiva
una cosa che qui non serve; questo garantisce le due che servono: che ogni skill dichiari a che
punto è la sua localizzazione, e che ogni skill localizzata sia datata e agganciata a fonti
ufficiali italiane o europee. Una norma che cambia non rompe nulla nel codice: l'unico modo di
accorgersene è una data che scade.

  python3 scripts/check-localization.py                 controllo strutturale (ogni push)
  python3 scripts/check-localization.py --strict-dates  anche le revisioni scadute sono errori
                                                        (workflow settimanale)
  python3 scripts/check-localization.py --today 2027-01-01   simula una data, per i test

Cosa verifica:
  1. Il registro è valido: ref unici, stati e livelli dal vocabolario chiuso.
  2. Il registro e l'albero coincidono: ogni SKILL.md pubblicata ha una riga, ogni riga core
     non `da-creare` ha la sua SKILL.md, nessuna skill `pro` è presente in questo repository.
  3. `da-localizzare`: la skill porta il banner che avvisa che i riferimenti sono ancora USA.
  4. `localizzata` / `nuova`: la skill porta la riga di revisione con la stessa data del registro,
     il rinvio a DISCLAIMER.md, almeno una fonte del catalogo con giurisdizione IT o EU pubblicata
     da un'autorità ufficiale, e nessuna fonte con giurisdizione USA.
  5. Le date: nessuna revisione nel futuro; una revisione più vecchia di `validita_giorni` è un
     avviso, o un errore con --strict-dates.
"""
import argparse
import datetime
import glob
import importlib.util
import os
import re
import sys
import tomllib
from urllib.parse import urlparse

REGISTRY = "localization/registry.toml"
STATI = {"universale", "da-localizzare", "localizzata", "da-creare", "nuova"}
LIVELLI = {"core", "pro"}
PACCHETTI = {"fisco", "lavoro", "appalti"}

# I segnaposto che lo script cerca nel testo della skill. Sono commenti HTML, quindi invisibili a
# chi legge il Markdown renderizzato ma stabili per il controllo.
BANNER = "<!-- eu-it: da-localizzare -->"
REVISIONE = re.compile(r"\*\*Revisione normativa:\*\*\s*(\d{4}-\d{2}-\d{2})")
DISCLAIMER = "DISCLAIMER.md"

# Autorità che fanno fede. Un dominio entra qui solo se chi lo pubblica è l'autorità stessa, non
# un aggregatore o una rivista: l'aggregatore è dove entrano i testi non aggiornati.
OFFICIAL_HOSTS = (
    "normattiva.it", "gazzettaufficiale.it", "eur-lex.europa.eu", "europa.eu",
    "agenziaentrate.gov.it", "garanteprivacy.it", "edpb.europa.eu", "agid.gov.it",
    "acn.gov.it", "csirt.gov.it", "anticorruzione.it", "acquistinretepa.it", "consip.it",
    "inps.it", "inail.it", "lavoro.gov.it", "ispettorato.gov.it", "cnel.it", "mimit.gov.it",
    "agcm.it", "agcom.it", "docs.italia.it", "developers.italia.it", "designers.italia.it",
    "italiadomani.gov.it", "padigitale2026.gov.it", "innovazione.gov.it", "governo.it",
    "uibm.gov.it", "euipo.europa.eu", "consob.it", "bancaditalia.it", "registroimprese.it",
    "fatturapa.gov.it", "pagopa.gov.it", "spid.gov.it", "cartaidentita.interno.gov.it",
    "accessibilita.agid.gov.it", "form.agid.gov.it",
)
USA = re.compile(r"^US(-[A-Z]{2})?$")


def official(url):
    host = urlparse(url).hostname or ""
    return any(host == h or host.endswith("." + h) for h in OFFICIAL_HOSTS)


def load_catalog():
    spec = importlib.util.spec_from_file_location("check_sources", "scripts/check-sources.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    by_skill = {}
    for _, entry in module.load():
        for ref in entry.get("skills", []):
            by_skill.setdefault(ref, []).append(entry)
    return by_skill


def published():
    """Ogni skill presente nell'albero pubblico, come `dipartimento:skill` -> percorso."""
    found = {}
    for path in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
        dept = path.split("/")[1]
        skill = os.path.basename(os.path.dirname(path))
        found[f"{dept}:{skill}"] = path
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict-dates", action="store_true")
    parser.add_argument("--today", help="data di riferimento, AAAA-MM-GG")
    args = parser.parse_args()
    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()

    if not os.path.exists(REGISTRY):
        print(f"  {REGISTRY} mancante")
        return 1
    with open(REGISTRY, "rb") as handle:
        rows = tomllib.load(handle).get("skill", [])

    problems, warnings = [], []
    departments = {p.split("/")[1] for p in glob.glob("plugins/*/.claude-plugin/plugin.json")}
    tree = published()
    catalog = load_catalog()
    seen = set()

    for row in rows:
        ref = row.get("ref", "")
        where = f"{REGISTRY}: {ref or '<senza ref>'}"
        if ref in seen:
            problems.append(f"{where}: ref duplicato")
        seen.add(ref)
        stato, livello = row.get("stato"), row.get("livello")
        if stato not in STATI:
            problems.append(f"{where}: stato {stato!r} non è uno di {', '.join(sorted(STATI))}")
            continue
        if livello not in LIVELLI:
            problems.append(f"{where}: livello {livello!r} non è uno di {', '.join(sorted(LIVELLI))}")
            continue
        prefix = ref.split(":", 1)[0]

        if livello == "pro":
            # Il contenuto pro non entra mai nel repository pubblico: una volta in git, è pubblico
            # per sempre, anche se poi viene cancellato.
            if row.get("pacchetto") not in PACCHETTI or prefix != row.get("pacchetto"):
                problems.append(f"{where}: una skill pro deve avere pacchetto in "
                                f"{', '.join(sorted(PACCHETTI))} e usarlo come prefisso")
            if glob.glob(f"plugins/*/skills/{ref.split(':', 1)[-1]}/SKILL.md"):
                problems.append(f"{where}: skill pro presente nel repository pubblico")
            continue

        if prefix not in departments:
            problems.append(f"{where}: dipartimento {prefix!r} non esiste in plugins/")
            continue
        path = tree.get(ref)
        if stato == "da-creare":
            if path:
                problems.append(f"{where}: la skill esiste — aggiorna lo stato a `nuova`")
            continue
        if not path:
            problems.append(f"{where}: stato {stato!r} ma {ref} non esiste in plugins/")
            continue
        text = open(path, encoding="utf-8").read()

        if stato == "da-localizzare" and BANNER not in text:
            problems.append(f"{path}: manca il banner {BANNER} (stato da-localizzare)")
        if stato in ("universale", "localizzata", "nuova") and BANNER in text:
            problems.append(f"{path}: porta il banner da-localizzare ma lo stato è {stato!r}")

        if stato in ("localizzata", "nuova"):
            declared = row.get("revisione")
            found = REVISIONE.search(text)
            if not declared:
                problems.append(f"{where}: manca `revisione` nel registro")
            elif not found:
                problems.append(f"{path}: manca la riga **Revisione normativa:** AAAA-MM-GG")
            elif found.group(1) != str(declared):
                problems.append(f"{path}: revisione {found.group(1)} diversa dal registro ({declared})")
            if DISCLAIMER not in text:
                problems.append(f"{path}: manca il rinvio a {DISCLAIMER}")
            sources = catalog.get(ref, [])
            if not any(e.get("jurisdiction") in ("IT", "EU") and official(e.get("url", ""))
                       for e in sources):
                problems.append(f"{path}: nessuna fonte ufficiale IT/UE nel catalogo sources/")
            # A US source can stay on a localized skill only when it is cited for method, not for
            # obligations (NIST 800-61 for incident handling, say), and the registry says so.
            allowed = set(row.get("fonti_usa_ammesse", []))
            for e in sources:
                if USA.match(e.get("jurisdiction", "")) and e.get("id") not in allowed:
                    problems.append(f"{path}: fonte USA {e['id']!r} su una skill localizzata — "
                                    f"togli la skill da `skills` in sources/ "
                                    f"o, se è citata solo per il metodo, aggiungila a fonti_usa_ammesse")
            if declared:
                date = declared if isinstance(declared, datetime.date) else datetime.date.fromisoformat(str(declared))
                if date > today:
                    problems.append(f"{where}: revisione {date} nel futuro")
                limit = row.get("validita_giorni", 365)
                if (today - date).days > limit:
                    message = (f"{where}: revisione {date} scaduta ({(today - date).days} giorni, "
                               f"limite {limit}) — ricontrolla le fonti e aggiorna la data")
                    (problems if args.strict_dates else warnings).append(message)

    for ref, path in tree.items():
        if ref not in seen:
            problems.append(f"{path}: skill non presente in {REGISTRY}")

    for w in warnings:
        print(f"  avviso: {w}")
    for p in problems:
        print(f"  {p}")
    core = sum(1 for r in rows if r.get("livello") == "core")
    done = sum(1 for r in rows if r.get("stato") in ("localizzata", "nuova"))
    print(f"localizzazione: {len(rows)} skill nel registro ({core} core), {done} localizzate o nuove, "
          f"{len(warnings)} avvisi, {len(problems)} problemi")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
