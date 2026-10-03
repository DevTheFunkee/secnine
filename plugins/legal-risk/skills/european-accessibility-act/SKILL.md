---
name: european-accessibility-act
description: Stabilisce se un prodotto o servizio digitale ricade nell'European Accessibility Act (Dir. UE 2019/882, recepita con D.Lgs. 82/2022) e cosa serve per rispettarlo — servizi soggetti come e-commerce e banca, deroga per le microimprese, requisiti tecnici EN 301 549, informazioni sull'accessibilità da pubblicare, regime transitorio. Usala per un sito o un'app rivolti ai consumatori, prima di consegnare un e-commerce a un cliente, quando arriva una contestazione sull'accessibilità, o per decidere se una microimpresa è esentata.
---

# European Accessibility Act

> **Revisione normativa:** 2026-10-03 · **Ambito:** UE e Italia · Applicabile dal 28 giugno 2025.
> Controlla in `references/sources.md` la versione vigente di EN 301 549 e le indicazioni AgID.
> Questa skill struttura la valutazione; non è consulenza legale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Chi è soggetto

L'EAA riguarda **prodotti e servizi rivolti ai consumatori**. Tra i servizi: commercio elettronico,
servizi bancari al consumo, comunicazioni elettroniche, e-book, siti e app dei servizi di trasporto
passeggeri. Tra i prodotti: computer, smartphone, terminali di pagamento, sportelli automatici,
biglietterie, lettori di e-book.

Non è soggetto il software puramente B2B: un gestionale venduto alle imprese no, l'e-commerce che
quella impresa apre ai consumatori sì.

**Microimprese.** Chi fornisce *servizi* ed è una microimpresa (meno di 10 persone e fatturato o
totale di bilancio non oltre 2 milioni di euro) è esentato. Per i prodotti l'esenzione non c'è,
ci sono solo obblighi alleggeriti. L'esenzione è del fornitore del servizio, non di chi lo
sviluppa: una software house piccola che costruisce l'e-commerce di un cliente più grande deve
consegnarlo conforme.

## Cosa serve

- **Requisiti tecnici.** In pratica EN 301 549, che richiama le WCAG al livello AA: percepibile,
  utilizzabile, comprensibile, robusto. L'audit con il metodo sta in `product:ux-product-auditor`.
- **Informazioni sull'accessibilità.** Il fornitore del servizio pubblica come il servizio soddisfa
  i requisiti (allegato V della direttiva), in formato accessibile. È un documento vivo: cambia
  quando cambia il servizio.
- **Onere sproporzionato.** Si può invocare solo con una valutazione documentata, da rifare
  periodicamente e da comunicare all'autorità; non è un'esenzione automatica.
- **Vigilanza.** Per i servizi in Italia vigila AgID, che riceve anche le segnalazioni degli utenti.

## Regime transitorio

I servizi già prestati con contratti stipulati prima del 28 giugno 2025 possono continuare fino alla
scadenza del contratto e comunque non oltre il 28 giugno 2030. Un nuovo rilascio o un nuovo
contratto non è "servizio esistente".

## Rapporto con la Legge Stanca

La PA e le grandi imprese private hanno già obblighi di accessibilità per L. 4/2004, con
dichiarazione annuale su piattaforma AgID: vedi `pa:accessibilita-pa`. L'EAA si aggiunge, non
sostituisce.

## Cosa restituire

1. Soggetto o no, con il ragionamento su tipo di servizio, destinatari e dimensione.
2. Gap principali rispetto a EN 301 549, in ordine di impatto sull'utente.
3. Bozza o revisione delle informazioni sull'accessibilità.
4. Rischi residui e cosa portare a un legale.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Considerare esentato un cliente perché la software house che sviluppa è una microimpresa.
- Dichiarare conforme un servizio senza un audit sui requisiti di EN 301 549.
- Invocare l'onere sproporzionato senza una valutazione scritta.
- Affidarsi a un overlay di accessibilità al posto della correzione del codice.
