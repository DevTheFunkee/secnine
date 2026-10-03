#!/usr/bin/env python3
"""Regenerate README.md (in Italian, SecNine edition) from the plugin tree. Run via ./scripts/check-all.sh --fix-readme,
and verified in CI so the README can never drift from what the repo actually contains."""
import glob, os, re, json, sys

# Display metadata per department. The department list itself comes from the plugin tree — see
# load_departments() — so a department cannot be added to disk and silently omitted from the docs.
# The rank fixes reporting order: the chief executive first, then the functions beneath.
META = {
    "executive":          (10, "Office of the CEO",   "Chief Executive"),
    "technology":         (20, "Technology",          "CTO / CIO"),
    "security":           (30, "Security",            "CISO"),
    "it-operations":      (35, "IT Operations",       "CIO"),
    "product":            (40, "Product",             "CPO"),
    "marketing":          (50, "Marketing",           "CMO"),
    "demand-generation":  (60, "Demand Generation",   "CMO"),
    "revenue":            (70, "Revenue",             "CRO"),
    "finance":            (80, "Finance",             "CFO"),
    "operations":         (90, "Operations",          "COO"),
    "pmo":                (95, "Program Management Office", "EPMO / COO"),
    "customer-experience": (100, "Customer Experience", "CCO"),
    "data-analytics":     (110, "Data & Analytics",   "CDO"),
    "corporate-strategy": (120, "Corporate Strategy", "CSO"),
    "people":             (130, "People",             "CHRO"),
    "legal-risk":         (140, "Legal & Risk",       "CLO / CCO"),
    "pa":                 (150, "Pubblica Amministrazione", "Head of Public Sector"),
}
REVIEWER = {"security", "legal-risk"}


def load_departments():
    """Departments come from disk, not from a list someone has to remember to update. A department
    present on disk but missing from META is a hard error rather than a silent omission — the same
    mistake used to drop a department out of both generated docs while --check still passed."""
    found = {os.path.basename(os.path.dirname(os.path.dirname(m)))
             for m in glob.glob("plugins/*/.claude-plugin/plugin.json")}
    missing = sorted(found - set(META))
    if missing:
        sys.exit("build-readme: no display metadata for department(s) "
                 + ", ".join(missing)
                 + "\n  add a (rank, title, executive) entry to META in scripts/build-readme.py")
    stale = sorted(set(META) - found)
    if stale:
        sys.exit("build-readme: META names department(s) that are not on disk: "
                 + ", ".join(stale)
                 + "\n  remove them from META in scripts/build-readme.py")
    return [(d, META[d][1], META[d][2]) for d in sorted(found, key=lambda d: META[d][0])]


ORDER = load_departments()


def _catalog_counts():
    """Catalog totals, read from the catalog so the README cannot claim a number it does not hold."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("check_sources", "scripts/check-sources.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    entries = module.load()
    skills = {ref for _, e in entries for ref in e.get("skills", [])}
    quotable = {"public-domain-usgov", "public-domain", "cc0", "cc-by", "open-data",
                "attribution-required"}
    return len(entries), len(skills), sum(1 for _, e in entries if e["license"] in quotable)


SOURCE_COUNT, SOURCE_SKILLS, SOURCE_QUOTABLE = _catalog_counts()


def summarize(path, limit=165):
    text = open(path, encoding="utf-8").read()
    front = re.match(r"^---\s*\n(.*?)\n---", text, re.S).group(1)
    desc = re.search(r"^description:\s*(.*)$", front, re.M).group(1).strip()
    cut = re.split(r"(?:\.\s+)(?:Also )?[Uu]se (?:this|it)\b", desc)[0]
    if len(cut) < 40:
        cut = desc
    cut = cut.rstrip(" .,—-")
    return cut[: limit - 1].rstrip() + "…" if len(cut) > limit else cut


def skills(dept):
    return sorted(glob.glob(f"plugins/{dept}/skills/*/SKILL.md"))


total = sum(len(skills(d)) for d, _, _ in ORDER)
# Badge counts come from the same tree walk as the tables below, so they cannot drift from
# reality — a wrong count fails `build-readme.py --check` in CI like any other staleness.
# Two bases, and the difference matters: the static `/badge/` endpoint takes a literal
# label-message-color triple, while the live endpoints hang off the root. Interpolating the
# `/badge` base into a `github/...` path produces a URL that returns a picture of itself.
SHIELDS = "https://img.shields.io"
B = f"{SHIELDS}/badge"
REPO = "DevTheFunkee/secnine"
UPSTREAM = "cbrock84/headcount"


def _localization_counts():
    """Stato della localizzazione, letto dal registro così il README non può dichiarare altro."""
    import collections
    import tomllib
    rows = tomllib.load(open("localization/registry.toml", "rb")).get("skill", [])
    core = [r for r in rows if r.get("livello") == "core"]
    by = collections.Counter(r["stato"] for r in core)
    pro = collections.Counter(r.get("pacchetto") for r in rows if r.get("livello") == "pro")
    return by, pro


LOC, PRO = _localization_counts()
LOCALIZED = LOC["localizzata"] + LOC["nuova"]

out = [
    '<h1 align="center">SecNine</h1>',
    "",
    '<p align="center"><b>Assumi un reparto, non un prompt. Per le imprese italiane ed europee.</b></p>',
    "",
    '<p align="center">',
    f'  <a href="AGENTS.md"><img alt="Funziona in Claude Code e ChatGPT"'
    f' src="{B}/funziona%20in-Claude%20Code%20%C2%B7%20ChatGPT-D97757?style=flat-square"></a>',
    f'  <img alt="{len(ORDER)} dipartimenti" src="{B}/dipartimenti-{len(ORDER)}-3F4B5B?style=flat-square">',
    f'  <img alt="{total} skill" src="{B}/skill-{total}-3F4B5B?style=flat-square">',
    f'  <a href="docs/LOCALIZZAZIONE.md"><img alt="{LOCALIZED} skill localizzate IT/UE"'
    f' src="{B}/localizzate%20IT%2FUE-{LOCALIZED}-009246?style=flat-square"></a>',
    f'  <a href="docs/SOURCES.md"><img alt="{SOURCE_COUNT} fonti citate"'
    f' src="{B}/fonti%20citate-{SOURCE_COUNT}-3F4B5B?style=flat-square"></a>',
    f'  <a href="LICENSE"><img alt="Licenza MIT" src="{B}/licenza-MIT-3F4B5B?style=flat-square"></a>',
    "</p>",
    "",
    '<p align="center">',
    f'  <a href="https://github.com/{REPO}/actions/workflows/checks.yml"><img alt="Controlli"'
    f' src="{SHIELDS}/github/actions/workflow/status/{REPO}/checks.yml?style=flat-square&label=controlli"></a>',
    f'  <a href="https://github.com/{REPO}/actions/workflows/revisioni.yml"><img alt="Revisioni normative"'
    f' src="{SHIELDS}/github/actions/workflow/status/{REPO}/revisioni.yml?style=flat-square&label=revisioni"></a>',
    f'  <a href="https://github.com/{REPO}/stargazers"><img alt="Stelle"'
    f' src="{SHIELDS}/github/stars/{REPO}?style=flat-square&color=3F4B5B"></a>',
    "</p>",
    "",
    "Un'organizzazione di agenti strutturata come un'azienda: una direzione generale sopra",
    f"{len(ORDER)} dipartimenti, {total} skill in tutto, adattata al mercato italiano ed europeo:",
    "GDPR con le prassi del Garante, NIS2, AI Act, accessibilità, fattura elettronica, Pubblica",
    "Amministrazione.",
    "",
    "Ogni dipartimento è un plugin che si installa da solo, così un progetto carica solo le funzioni",
    "che gli servono.",
    "",
    "> **Non sostituisce commercialista, consulente del lavoro o avvocato.** Le skill strutturano il",
    "> problema e dicono cosa chiedere; le decisioni con effetti fiscali, lavoristici o legali vanno",
    "> validate da un professionista. Vedi [DISCLAIMER.md](DISCLAIMER.md).",
    "",
    "## Installazione",
    "",
    "**[Claude Code](https://claude.com/claude-code)**",
    "",
    "```",
    f"/plugin marketplace add {REPO}",
    "/plugin install legal-risk@secnine",
    "/plugin install pa@secnine",
    "```",
    "",
    "**ChatGPT e Codex**: lo stesso repository. Aggiungilo come marketplace di plugin, oppure copia il",
    "dipartimento che ti serve in `.agents/skills/` nel tuo progetto. Le skill sono identiche, cambiano",
    "solo i manifest, generati dallo stesso albero. Vedi `AGENTS.md`.",
    "",
    "Le skill si indirizzano come `dipartimento:skill` (`legal-risk:nis2-compliance`,",
    "`finance:fatturazione-elettronica-sdi`), quindi i nomi non collidono.",
    "",
    "## Uso",
    "",
    "Le skill si attivano da sole quando la richiesta corrisponde:",
    "",
    "| Chiedi | Cosa si attiva |",
    "|---|---|",
    "| \"siamo soggetti alla NIS2?\" | `legal-risk:nis2-compliance` |",
    "| \"perché SDI mi ha scartato la fattura?\" | `finance:fatturazione-elettronica-sdi` |",
    "| \"il nostro chatbot rientra nell'AI Act?\" | `legal-risk:eu-ai-act-compliance` |",
    "| \"dobbiamo integrare SPID e pagoPA per il comune\" | `pa:piattaforme-abilitanti` |",
    "| \"rivedi questo design prima di svilupparlo\" | `security:threat-modeling` |",
    "",
    "Oppure chiamane una per nome: `/legal-risk:privacy-and-data-protection`.",
    "",
    "## Stato della localizzazione",
    "",
    "Ogni skill ha una riga in [`localization/registry.toml`](localization/registry.toml) che dice a",
    "che punto è, e la CI la verifica a ogni push:",
    "",
    "| Stato | Skill | Significato |",
    "|---|---|---|",
    f"| universale | {LOC['universale']} | Metodo valido ovunque, testo upstream in inglese |",
    f"| localizzata | {LOC['localizzata']} | Riscritta per IT/UE, datata, con fonti ufficiali |",
    f"| nuova | {LOC['nuova']} | Creata per IT/UE, datata, con fonti ufficiali |",
    f"| da localizzare | {LOC['da-localizzare']} | Riferimenti ancora USA: la skill lo dichiara in testa |",
    f"| da creare | {LOC['da-creare']} | In programma per il core pubblico |",
    "",
    "Le skill localizzate portano una **data di revisione normativa**. Un controllo settimanale fallisce",
    "quando una revisione è scaduta, perché una norma cambia senza che cambi nulla nel codice.",
    "",
    "## Core pubblico e pacchetti pro",
    "",
    "Questo repository è il core open source. Le aree che richiedono aggiornamento continuo e hanno",
    "rischio professionale alto sono pacchetti privati in abbonamento, curati da Bitlore:",
    "",
    f"- **fisco** ({PRO['fisco']} skill): IVA, regime forfettario, F24 e scadenzario, crediti d'imposta, corrispettivi.",
    f"- **lavoro** ({PRO['lavoro']} skill): CCNL e inquadramento, TFR e previdenza complementare, welfare aziendale.",
    f"- **appalti** ({PRO['appalti']} skill): Codice appalti, MePA e Consip, documentazione di gara, fatturazione verso PA, PNRR.",
    "",
    "Info: [secnine.it](https://secnine.it) · [bitlore.it](https://bitlore.it)",
    "",
    "## Dipartimenti",
    "",
]
for dept, title, exec_role in ORDER:
    paths = skills(dept)
    tag = " · **reviewer**" if dept in REVIEWER else ""
    out += [f"<details>", f"<summary><b>{title}</b> ({exec_role}) — {len(paths)} skill{tag}</summary>", "",
            "| Skill | Cosa fa |", "|---|---|"]
    for p in paths:
        out.append(f"| `{os.path.basename(os.path.dirname(p))}` | {summarize(p)}. |")
    out += ["", "</details>", ""]

out += [
    "I **dipartimenti reviewer** (`security`, `legal-risk`) rivedono ciò che costruiscono gli altri, e",
    "i loro blocchi non sono scavalcabili dal dipartimento sotto revisione.",
    "",
    "## Fonti",
    "",
    f"{SOURCE_COUNT} fonti su {SOURCE_SKILLS} skill: Normattiva, EUR-Lex, Garante, ACN, AgID, Agenzia",
    "delle Entrate, ANAC e le fonti tecniche internazionali. Ogni skill le trova in",
    "`references/sources.md`. [Indice completo in `docs/SOURCES.md`](docs/SOURCES.md).",
    "",
    "**Riferimenti, mai copie**: ogni voce dice cosa si può farne. I testi di legge italiani ed europei",
    "sono citabili; le pagine delle autorità e le norme tecniche si leggono e si citano.",
    f"{SOURCE_QUOTABLE} delle {SOURCE_COUNT} sono riproducibili.",
    "",
    "## Come è organizzato",
    "",
    "```",
    "plugins/<dipartimento>/",
    "  .claude-plugin/plugin.json   manifest del dipartimento, Claude Code",
    "  .codex-plugin/plugin.json    lo stesso dipartimento, ChatGPT e Codex",
    "  skills/<skill>/SKILL.md      il nome nel frontmatter è uguale alla cartella",
    "  skills/<skill>/references/   file di supporto, comprese le fonti della skill",
    "localization/registry.toml     stato di localizzazione, livello core/pro e data di revisione",
    "sources/*.toml                 catalogo delle fonti, collegato alle skill",
    ".claude/agents/<id>.md         un charter per dipartimento",
    "docs/LOCALIZZAZIONE.md         come si localizza una skill e come si rivede",
    "docs/AGENT-SURFACES.md         ogni percorso ha un solo proprietario, verificato in CI",
    "docs/DECISION-LOG.md           decisioni numerate, upstream e IT/UE",
    "DISCLAIMER.md                  limiti d'uso professionali",
    "docs/ORIGINE.md                origine del progetto e attribuzioni",
    "```",
    "",
    "## Contribuire",
    "",
    "```",
    "./scripts/check-all.sh",
    "```",
    "",
    "Tutti i controlli della CI in un solo script. Per localizzare una skill segui",
    "[docs/LOCALIZZAZIONE.md](docs/LOCALIZZAZIONE.md); per tutto il resto [CONTRIBUTING.md](CONTRIBUTING.md).",
    "",
    "## Origine e licenza",
    "",
    f"SecNine deriva da [headcount](https://github.com/{UPSTREAM}) di",
    "[Chris Brock](https://chrisbrock.io), rilasciato con licenza MIT. Architettura, skill universali e",
    "strumenti di build sono suoi; localizzazione IT/UE, dipartimento PA e controlli di revisione sono di",
    "[Bitlore](https://bitlore.it). Dettagli in [docs/ORIGINE.md](docs/ORIGINE.md).",
    "",
    "MIT, vedi [LICENSE](LICENSE).",
    "",
    "---",
    "",
    "<sub>README generato da `scripts/build-readme.py`: modifica quello, non questo file.</sub>",
    "",
]
content = "\n".join(out)

# The org chart's department table drifts the same way the README did. Generate it between
# markers so the two cannot disagree; the analysis prose around it stays hand-written.
chart_rows = "\n".join(
    f"| `{d}` | {t} | {e} | {len(skills(d))}"
    + (" · reviewer-class |" if d in REVIEWER else " |")
    for d, t, e in ORDER
)
chart_block = (
    "<!-- BEGIN GENERATED: departments -->\n"
    f"| Department | Function | Executive | Skills |\n|---|---|---|---|\n{chart_rows}\n"
    f"\n{len(ORDER)} departments, {total} skills.\n"
    "<!-- END GENERATED: departments -->"
)
chart_path = "docs/org-chart.md"
chart_current = open(chart_path, encoding="utf-8").read()
chart_new = re.sub(
    r"<!-- BEGIN GENERATED: departments -->.*?<!-- END GENERATED: departments -->",
    lambda _: chart_block,
    chart_current,
    flags=re.S,
)

if "--check" in sys.argv:
    if chart_current != chart_new:
        print("  docs/org-chart.md department table is stale — run: python3 scripts/build-readme.py")
        sys.exit(1)
    current = open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else ""
    if current != content:
        print("  README.md is stale — run: python3 scripts/build-readme.py")
        sys.exit(1)
    print("README is current")
    sys.exit(0)

open("README.md", "w", encoding="utf-8").write(content)
open(chart_path, "w", encoding="utf-8").write(chart_new)
print(f"README.md and org-chart.md regenerated — {len(ORDER)} departments, {total} skills")
