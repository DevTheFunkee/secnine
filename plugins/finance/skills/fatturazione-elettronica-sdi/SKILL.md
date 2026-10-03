---
name: fatturazione-elettronica-sdi
description: Imposta e controlla la fatturazione elettronica italiana via Sistema di Interscambio — tracciato FatturaPA, codice destinatario e PEC, tipi documento e codici natura, termini di emissione, scarti e notifiche SDI, imposta di bollo, operazioni con l'estero, conservazione — sia dal lato di chi fattura sia dal lato di chi sviluppa un gestionale che integra SDI. Usala per emettere o correggere una fattura elettronica, capire uno scarto, scegliere il canale di trasmissione, progettare l'integrazione SDI in un software, o controllare un flusso di fatturazione prima di un controllo.
---

# Fatturazione elettronica e SDI

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia · Le specifiche tecniche FatturaPA
> cambiano per versione (nuovi tipi documento, nuovi controlli): verifica sempre la versione
> corrente in `references/sources.md` prima di dare un codice.
> Questa skill struttura il problema; per il trattamento IVA di un'operazione decide il
> commercialista. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Il modello mentale

Una fattura elettronica esiste solo se SDI l'ha accettata. Il file XML che hai generato non è una
fattura finché non arriva la ricevuta di consegna o di impossibilità di recapito; uno scarto
significa che la fattura **non è stata emessa**. Quasi tutti gli errori operativi nascono dal
trattare l'invio come emissione.

## Il flusso

1. **Generazione** dell'XML nel formato FatturaPA: `FPR12` verso privati, `FPA12` verso la PA (dove
   la firma digitale è obbligatoria; verso privati è facoltativa).
2. **Trasmissione** a SDI per uno dei canali: web service SdICoop o SFTP (richiedono accreditamento,
   adatti a un gestionale ad alto volume), PEC, portale Fatture e Corrispettivi, oppure un
   intermediario.
3. **Controlli SDI** sul file, poi notifica: ricevuta di consegna, mancata consegna (la fattura è
   comunque emessa e il cliente la trova nella sua area riservata), o scarto con codice di errore.
4. **Recapito** al codice destinatario (7 caratteri) o alla PEC del cliente; verso la PA al codice
   univoco ufficio (6 caratteri) dall'Indice PA. Se il cliente privato non comunica nulla si usa
   `0000000` e gli si consegna una copia di cortesia.

## Termini

La fattura immediata si trasmette entro 12 giorni dall'operazione; la differita (tipo `TD24`), per
cessioni documentate da DDT o prestazioni con idonea documentazione, entro il 15 del mese successivo.
Data della fattura e data di trasmissione possono quindi essere diverse, e devono essere coerenti.

## Codici che si sbagliano più spesso

- **Tipo documento:** `TD01` fattura, `TD04` nota di credito, `TD24` differita, `TD16`–`TD19`
  integrazioni e autofatture per reverse charge interno ed estero.
- **Natura** per le operazioni senza IVA, con il sotto-codice obbligatorio: ad esempio `N2.2` per
  le operazioni non soggette dei contribuenti forfettari, `N6.x` per il reverse charge. La natura
  sbagliata non viene sempre scartata, ma rende la fattura sbagliata.
- **Imposta di bollo:** 2 euro sulle fatture senza IVA oltre 77,47 euro, indicata nel tracciato;
  l'Agenzia calcola il dovuto per trimestre e si versa con F24.

## Scarti

Uno scarto si gestisce entro 5 giorni dalla notifica: si ritrasmette il documento corretto con
lo stesso numero e la stessa data, oppure con un nuovo numero collegato all'originale secondo le
indicazioni dell'Agenzia. Il codice di errore dice quale controllo è fallito: leggilo prima di
toccare il file. Un gestionale deve conservare ogni notifica SDI legata al documento.

## Estero

Le operazioni con clienti esteri passano anch'esse da SDI con codice destinatario `XXXXXXX`; gli
acquisti da fornitori esteri si integrano con autofattura `TD17`–`TD19`. È l'ex esterometro, oggi
dentro lo stesso flusso.

## Conservazione

Conservazione digitale a norma per 10 anni. L'Agenzia offre un servizio gratuito previa adesione;
un gestionale che lo sostituisce deve appoggiarsi a un conservatore qualificato.

## Per chi sviluppa l'integrazione

- Valida l'XML contro lo schema XSD della versione corrente prima dell'invio, non dopo lo scarto.
- Rendi idempotente la trasmissione: lo stesso documento non deve partire due volte per un retry.
- Modella lo stato della fattura sulle notifiche SDI (inviata, consegnata, non consegnata,
  scartata), non sul successo della chiamata HTTP.
- Tratta ogni nuova versione delle specifiche come un rilascio con date: l'Agenzia pubblica la data
  da cui i nuovi controlli diventano bloccanti.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Considerare emessa una fattura scartata da SDI.
- Correggere una fattura consegnata modificandola: si emette una nota di credito.
- Indicare un codice natura senza sotto-codice.
- Generare XML senza validarlo contro lo schema della versione in vigore.
