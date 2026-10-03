---
name: head-of-public-sector
description: Guida il lavoro con la Pubblica Amministrazione italiana — decidere se e come vendere alla PA, cosa preparare prima della prima gara, quali regole tecniche AgID e quali piattaforme incontrerà il progetto, come si viene pagati, e quando passare la questione a legal-risk o a un consulente appalti. Usala quando un'azienda valuta il mercato pubblico, quando arriva una richiesta da un ente, per preparare un'offerta su MePA, o per orientarsi tra Codice appalti, CAD e linee guida AgID.
---

# Head of Public Sector

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia · Soglie e procedure del Codice
> appalti cambiano con i correttivi: verifica sul testo vigente in `references/sources.md`.
> Questa skill orienta; per partecipare a una gara serve chi conosce il Codice. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## La decisione prima della gara

La PA è un cliente affidabile nei pagamenti e lento in tutto il resto. Prima di investirci chiediti:

- **Ciclo di vendita.** Mesi, non settimane: programmazione dell'ente, procedura, stipula, collaudo.
- **Requisiti.** Senza i requisiti generali e, sopra certe soglie, quelli speciali (fatturato
  specifico, referenze, certificazioni) non si partecipa. Si costruiscono prima, non durante.
- **Margini.** Il prezzo è spesso il criterio decisivo o pesa molto; le penali sono contrattuali.
- **Vincoli di prodotto.** Software commissionato e pagato dalla PA va rilasciato in open source
  (art. 69 CAD): il modello di business deve prevederlo.

## Cosa serve prima della prima offerta

- PEC, firma digitale, abilitazione su MePA nelle categorie giuste (`acquistinretepa.it`).
- Requisiti generali in ordine: nessuna causa di esclusione (artt. 94–98 Codice), DURC regolare,
  regolarità fiscale. ANAC li verifica tramite il fascicolo virtuale dell'operatore economico.
- Conto corrente dedicato per la tracciabilità dei flussi finanziari (L. 136/2010).
- Un modello di offerta tecnica riusabile e referenze documentate.

## Le procedure, in una frase ciascuna

Sotto i 140.000 euro per servizi e forniture l'ente può affidare direttamente, rispettando il
principio di rotazione; sopra, e fino alla soglia europea, si usa la procedura negoziata con
inviti; sopra la soglia europea le procedure ordinarie. Gli strumenti Consip (convenzioni, accordi
quadro, MePA) sono spesso obbligatori per l'ente. Il dettaglio operativo sta nel pacchetto
privato *appalti* di SecNine.

## Regole tecniche che il progetto incontrerà

- Linee guida AgID su sviluppo, riuso e interoperabilità: `pa:linee-guida-agid-sviluppo`.
- SPID, CIE, pagoPA, App IO, PDND: `pa:piattaforme-abilitanti`.
- Accessibilità e dichiarazione annuale: `pa:accessibilita-pa`.
- Servizi cloud qualificati ACN se il servizio gira in cloud per l'ente.
- Privacy: l'ente è titolare, il fornitore è quasi sempre responsabile del trattamento
  (`legal-risk:privacy-and-data-protection`).

## Come si viene pagati

Fattura elettronica `FPA12` firmata al codice univoco ufficio, con CIG (e CUP se il progetto è
d'investimento), IVA in split payment; termini di pagamento di 30 giorni salvo eccezioni. La
fattura senza CIG o al codice ufficio sbagliato viene rifiutata dall'ente. Vedi
`finance:fatturazione-elettronica-sdi`.

## Quando passare la mano

- Clausole contrattuali, penali, subappalto, raggruppamenti: `legal-risk:contract-review`.
- Requisiti dubbi, esclusioni, ricorsi: consulente appalti o avvocato amministrativista.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Partecipare a una gara senza aver verificato i requisiti di partecipazione.
- Promettere tempi di incasso senza CIG, codice ufficio e regolarità DURC verificati.
- Vendere alla PA software custom senza aver previsto il rilascio in open source.
- Dare una soglia o un termine del Codice senza controllarli sul testo vigente.
