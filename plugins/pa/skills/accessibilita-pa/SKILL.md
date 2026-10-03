---
name: accessibilita-pa
description: Rende conformi siti e app della Pubblica Amministrazione e delle grandi imprese obbligate alla Legge Stanca (L. 4/2004) — requisiti tecnici EN 301 549 e WCAG, dichiarazione di accessibilità e obiettivi annuali su piattaforma AgID, meccanismo di feedback, ruolo del difensore civico per il digitale. Usala quando consegni un sito o un'app a un ente pubblico, per preparare o aggiornare la dichiarazione di accessibilità, per un audit prima del collaudo, o quando un utente segnala un problema di accessibilità.
---

# Accessibilità nella PA

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia · Scadenze annuali e modelli di
> dichiarazione li fissa AgID: verifica in `references/sources.md` prima di indicare una data.
> Questa skill struttura l'adempimento; non è consulenza legale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Chi è obbligato

Le pubbliche amministrazioni e i soggetti assimilati, e dal 2020 anche i privati con fatturato
medio superiore a 500 milioni di euro nell'ultimo triennio, per i servizi offerti tramite siti e
app. Per i servizi ai consumatori dei privati si aggiunge l'European Accessibility Act:
`legal-risk:european-accessibility-act`.

## Cosa serve

- **Conformità tecnica** ai requisiti delle linee guida AgID, che rinviano a EN 301 549 e quindi
  alle WCAG al livello AA. Per il metodo di audit `product:ux-product-auditor`.
- **Dichiarazione di accessibilità** per ogni sito e app, compilata sulla piattaforma AgID con il
  modello ufficiale, pubblicata con un link nel footer e aggiornata ogni anno (scadenza AgID: di
  norma il 23 settembre).
- **Meccanismo di feedback**: un canale per segnalare problemi e chiedere contenuti in forma
  accessibile, con risposta entro 30 giorni. Se la risposta manca o non soddisfa, l'utente si
  rivolge al difensore civico per il digitale.
- **Obiettivi di accessibilità** annuali dell'ente (di norma entro il 31 marzo).

## Per chi sviluppa per un ente

- L'accessibilità è criterio di collaudo: inseriscila nella definizione di pronto, non in un audit
  finale.
- Usa i componenti Bootstrap Italia e i modelli Designers Italia, che partono accessibili; le
  personalizzazioni sono dove la conformità si perde.
- Consegna all'ente l'esito dell'audit con le non conformità residue: gli serve per compilare la
  dichiarazione, che è sua.
- I documenti scaricabili (PDF, moduli) sono contenuti del sito e devono essere accessibili anche
  loro.

## Cosa restituire

1. Esito dell'audit per requisito, con le non conformità ordinate per impatto.
2. Testo da inserire nella dichiarazione, comprese le parti non accessibili e le alternative.
3. Piano di correzione con date, da collegare agli obiettivi annuali dell'ente.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Dichiarare un sito "conforme" senza un audit sui requisiti di EN 301 549.
- Pubblicare un sito per la PA senza meccanismo di feedback.
- Usare un overlay di accessibilità al posto della correzione del codice.
- Compilare la dichiarazione al posto dell'ente senza che l'ente la approvi.
