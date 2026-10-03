# Localizzazione IT/UE

Come SecNine passa da una skill pensata per gli Stati Uniti a una skill affidabile per un'impresa
italiana, e come la mantiene affidabile quando la norma cambia.

## Il registro

`localization/registry.toml` ha una riga per ogni skill del prodotto, pubblica o privata. È nato
dalla mappa delle 172 skill upstream (116 universali, 56 da localizzare, più 31 da creare) e da
allora si mantiene a mano, nella stessa PR che cambia la skill.

| Campo | Valori | Note |
|---|---|---|
| `ref` | `dipartimento:skill` o `pacchetto:skill` | Per le skill pro il prefisso è il pacchetto |
| `dipartimento` | uno dei 17 | Il dipartimento di competenza, anche per le pro |
| `stato` | `universale`, `da-localizzare`, `localizzata`, `da-creare`, `nuova` | |
| `livello` | `core`, `pro` | `pro` non entra mai in questo repository |
| `pacchetto` | `fisco`, `lavoro`, `appalti` | Solo per `pro` |
| `revisione` | data | Solo `localizzata` e `nuova`; uguale a quella scritta nella skill |
| `validita_giorni` | intero | 180 per finance, people e pa (cambiano con la legge di bilancio), 365 altrove |
| `fonti_usa_ammesse` | lista di id | Fonti USA tenute solo per il metodo, mai per gli obblighi |
| `motivo`, `fonti_it` | testo | Dalla mappa: perché va localizzata e dove guardare |

## Cosa verifica la CI

`scripts/check-localization.py`, a ogni push:

- registro e albero coincidono: nessuna skill senza riga, nessuna riga senza skill (salvo
  `da-creare`), nessuna skill `pro` sotto `plugins/`;
- ogni skill `da-localizzare` porta il banner `<!-- eu-it: da-localizzare -->` con l'avviso in
  italiano e le fonti da usare al posto di quelle USA;
- ogni skill `localizzata` o `nuova` porta la riga `**Revisione normativa:** AAAA-MM-GG` uguale al
  registro, il rinvio a `DISCLAIMER.md`, almeno una fonte del catalogo con giurisdizione IT o EU
  pubblicata da un'autorità ufficiale, e nessuna fonte USA non dichiarata;
- nessuna revisione nel futuro. Una revisione scaduta è un avviso.

Il workflow `revisioni.yml` esegue lo stesso controllo con `--strict-dates` ogni lunedì: lì una
revisione scaduta è un errore. Si sistema rileggendo le fonti e aggiornando la data nella skill e
nel registro, mai spostando la data senza rileggere.

## Come localizzare una skill

1. Leggi la riga del registro: `motivo` e `fonti_it` dicono cosa cambia.
2. Aggiungi le fonti ufficiali in `sources/it-eu-*.toml` (Normattiva con URN, EUR-Lex con ELI,
   pagine delle autorità) e togli la skill dalle fonti USA che non servono più.
3. Riscrivi la skill in italiano mantenendo la forma upstream: frontmatter `name` e `description`
   (con i casi d'uso), intestazione con revisione e disclaimer, corpo con regole concrete, una
   sezione `## Fonti` e una sezione `## Never` con imperativi coerenti.
4. Togli il banner, aggiorna stato e `revisione` nel registro.
5. `python3 scripts/build-sources.py && python3 scripts/build-readme.py && ./scripts/check-all.sh`.

Le skill universali restano in inglese come upstream: così le correzioni possono andare e tornare
tra i due progetti.

## Core e pro

Il core pubblico contiene tutto ciò che è metodo o normativa relativamente stabile. I pacchetti
privati raccolgono le aree dove il cliente paga la manutenzione, perché le regole cambiano ogni anno
e l'errore costa:

| Pacchetto | Skill | Dipartimento |
|---|---|---|
| `fisco` | iva, regime-forfettario, f24-e-scadenzario-fiscale, agevolazioni-e-crediti-imposta, corrispettivi-telematici | finance |
| `lavoro` | ccnl-e-inquadramento, tfr-e-previdenza-complementare, welfare-aziendale | people |
| `appalti` | codice-appalti, mepa-e-consip, requisiti-e-documentazione-gara, fatturazione-verso-pa, fondi-pnrr-e-bandi | pa |

I pacchetti pro vivono in un repository privato con lo stesso formato (marketplace, plugin per
pacchetto, stessi controlli) e si installano accanto al core:
`/plugin install fisco@secnine-pro`. Le skill core possono citarli per nome nel testo, ma non come
riferimento `dipartimento:skill` verificato, perché qui non esistono.
