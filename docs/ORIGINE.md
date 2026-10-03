# Origine del progetto

SecNine è un'opera derivata da **headcount** di Chris Brock
(<https://github.com/cbrock84/headcount>), rilasciato con licenza MIT. Il copyright e il testo della
licenza originali sono conservati in [LICENSE](LICENSE), come la licenza richiede.

## Cosa viene dall'upstream

- L'architettura: marketplace, un plugin per dipartimento, `SKILL.md`, charter in `.claude/agents/`,
  mappa delle superfici, catalogo delle fonti, generatori e controlli in `scripts/`.
- Le skill marcate `universale` e `da-localizzare` in `localization/registry.toml`, nel loro testo
  originale in inglese. Le seconde portano in testa un avviso in italiano aggiunto da Bitlore.
- Le decisioni numerate D1–D-n in `docs/DECISION-LOG.md`.

## Cosa aggiunge Bitlore

- Le skill marcate `localizzata` e `nuova` nel registro, e il dipartimento `pa`.
- Il registro di localizzazione, `scripts/check-localization.py` e il workflow delle revisioni.
- Il catalogo delle fonti IT/UE (`sources/it-eu-*.toml`).
- README, DISCLAIMER e documentazione in italiano; le decisioni D-IT in `docs/DECISION-LOG.md`.

## Cosa è stato tolto

- I verticali statunitensi `industrial` ed `education` e le relative fonti (decisione D-IT3).
- Il controllo di ortografia US-English (decisione D-IT2).

SecNine non è affiliato a Chris Brock né da lui approvato.
