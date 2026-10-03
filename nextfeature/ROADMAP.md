# Roadmap SecNine — prossimi passi

Aggiornata al 2026-10-03, dopo il merge della PR #1 (edizione IT/UE di headcount su `main`).
Ogni voce ha un obiettivo, cosa serve per farla e il criterio con cui la consideriamo chiusa.
I numeri sul registro vengono da `localization/registry.toml` (203 skill: 116 universali,
54 da localizzare, 22 da creare, 11 già localizzate o nuove).

| # | Voce | Stato |
|---|---|---|
| 1 | Merge della PR #1 | fatto |
| 2 | SecNine sul sito Bitlore | in corso |
| 3 | Test sul campo nel repo bitlore | da fare |
| 4 | Skill ancora da localizzare o creare | da fare |
| 5 | Issue a Chris Brock (upstream headcount) | da fare |
| 6 | Pacchetto privato secnine-pro | da fare, dopo trazione |

---

## 1. Merge della PR #1 — fatto

- **Obiettivo:** portare su `main` la struttura IT/UE (17 dipartimenti, registro di
  localizzazione, controllo `check-localization.py`, workflow settimanale delle revisioni).
- **Cosa serviva:** revisione di Matteo, CI verde.
- **Completamento:** PR #1 mergiata su `main` (commit `450f311`). ✓

## 2. SecNine sul sito Bitlore — in corso

- **Obiettivo:** SecNine è la vetrina di Bitlore. Una pagina o sezione su bitlore.it che lo
  presenta e porta a consulenze.
- **Cosa serve:**
  - pagina o sezione su bitlore.it (repo `DevTheFunkee/bitlore`) con link a
    `github.com/DevTheFunkee/secnine`, riepilogo dei 17 dipartimenti e contatto per consulenze;
  - DNS di `secnine.it` e `secnine.eu` puntati alla pagina Bitlore o a una landing dedicata;
  - link inverso dal README di SecNine a bitlore.it (il README è generato: va modificato
    `scripts/build-readme.py`, non il file).
- **Completamento:** la pagina è online, i due domini rispondono e portano lì, il README di
  SecNine linka Bitlore. Il lavoro sul repo bitlore è in corso in un thread separato.

## 3. Test sul campo nel repo bitlore

- **Obiettivo:** usare SecNine sul codice vero di Bitlore e ricavarne la prova da mostrare in
  vetrina.
- **Cosa serve:**
  - installare dal marketplace i dipartimenti `technology`, `product`, `security`,
    `legal-risk`, `marketing`, `executive` nel repo `DevTheFunkee/bitlore`;
  - eseguire una security review (`security`, `security-review`) e una code review
    (`technology`) sul codice Bitlore;
  - annotare cosa ha funzionato, cosa no e quali skill mancano o sbagliano in contesto italiano.
- **Completamento:** report delle due review salvato e pubblicabile (senza dati sensibili),
  issue aperte su questo repo per ogni difetto delle skill emerso, un caso d'uso aggiunto a
  `docs/USE-CASES.md`.

## 4. Skill ancora da localizzare o creare

- **Obiettivo:** chiudere il debito di localizzazione del core pubblico, partendo dai
  dipartimenti che vendono di più (`legal-risk` e `people`).
- **Cosa serve, per ogni skill:** testo in italiano, `## Fonti` con almeno una fonte ufficiale
  IT/UE, rimando a DISCLAIMER.md, data di revisione allineata al registro, stato aggiornato
  in `localization/registry.toml` (`da-localizzare` → `localizzata`, `da-creare` → `nuova`),
  fonte aggiunta in `sources/*.toml` e `scripts/build-sources.py` rigenerato.
- **Completamento:** `scripts/check-localization.py` passa e il registro non ha più righe core
  in stato `da-localizzare` o `da-creare`.

### 4a. Da localizzare: 54 skill core

In ordine di priorità.

| Dipartimento | N. | Skill |
|---|---|---|
| legal-risk | 6 | chief-legal-and-risk-officer, contract-review, corporate-governance, disputes-and-legal-holds, intellectual-property, regulatory-compliance |
| people | 10 | benefits-and-leave, chief-human-resources-officer, compensation-and-leveling, employee-relations, employment-compliance, hiring-and-interviewing, learning-and-development, onboarding-and-offboarding, payroll-operations, performance-management |
| finance | 8 | capital-structure-and-covenants, chief-financial-officer, financial-reporting-and-close, financial-statement-analysis, internal-controls-and-audit, revenue-recognition, tax, treasury-and-liquidity |
| demand-generation | 6 | account-based-marketing, landing-page-cro-expert, lead-capture, lifecycle-messaging, marketing-analytics, paid-advertising |
| marketing | 6 | behavioral-marketing, marketing-copywriting, newsletter-writer, partnership-marketing, social-post-craft, youtube-producer |
| revenue | 5 | deal-negotiation, outbound-prospecting, pricing-and-packaging, retention, sales-compensation-and-territory |
| customer-experience | 3 | customer-onboarding-and-implementation, self-service-and-knowledge, support-operations |
| data-analytics | 2 | ai-ml-governance, data-governance |
| executive | 2 | chief-executive, fundraising-and-investor-relations |
| product | 2 | product-requirements, ux-product-auditor |
| corporate-strategy | 1 | mergers-and-acquisitions |
| it-operations | 1 | telephony-and-conferencing |
| operations | 1 | facilities-and-workplace |
| security | 1 | chief-information-security-officer |

### 4b. Da creare: 10 skill core nuove

| Dipartimento | Skill |
|---|---|
| legal-risk | codice-del-consumo, cyber-resilience-act, digital-services-act, gdpr-prassi-garante, modello-231-e-whistleblowing |
| people | lavoro-agile, sicurezza-sul-lavoro, tipologie-contrattuali |
| pa | cloud-qualificato-pa, design-servizi-pubblici |

### 4c. Debito collegato

- `docs/org-chart.html` ancora in inglese.
- Gli URL delle fonti IT/UE non sono stati verificati online: va fatto un giro di verifica con
  `scripts/check-sources.py` da una rete senza blocchi.

## 5. Issue a Chris Brock (upstream headcount)

- **Obiettivo:** visibilità a costo zero e un canale per far fluire le correzioni in entrambe
  le direzioni.
- **Cosa serve:** una issue su `cbrock84/headcount` che segnala il fork (licenza MIT rispettata,
  vedi `docs/ORIGINE.md`) e propone un layer regionale generico: registro di localizzazione
  e controllo come meccanismo upstream, contenuti per paese nei fork.
- **Completamento:** issue aperta e risposta ricevuta; se la proposta passa, una PR upstream
  con il meccanismo del registro senza contenuti italiani.

## 6. Pacchetto privato secnine-pro

- **Obiettivo:** la parte in abbonamento dell'open core: fisco, lavoro e appalti.
- **Quando:** dopo che il core pubblico ha un minimo di trazione (stelle, installazioni o
  prime consulenze arrivate dal sito Bitlore).
- **Cosa serve:** le 12 skill pro ancora da creare nel repo privato `DevTheFunkee/secnine-pro`
  (`appalti:codice-appalti` è già scritta):

  | Pacchetto | Skill |
  |---|---|
  | fisco | agevolazioni-e-crediti-imposta, corrispettivi-telematici, f24-e-scadenzario-fiscale, iva, regime-forfettario |
  | lavoro | ccnl-e-inquadramento, tfr-e-previdenza-complementare, welfare-aziendale |
  | appalti | fatturazione-verso-pa, fondi-pnrr-e-bandi, mepa-e-consip, requisiti-e-documentazione-gara |

  Più il modello di distribuzione (accesso al marketplace privato) e il prezzo.
- **Completamento:** i tre pacchetti installabili dal marketplace privato, registro senza righe
  pro in stato `da-creare`, nessun contenuto pro in questo repo (lo garantisce già
  `check-localization.py`).
