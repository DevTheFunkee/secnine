---
name: eu-ai-act-compliance
description: Classifica un sistema di intelligenza artificiale secondo l'AI Act (Reg. UE 2024/1689) e la legge italiana sull'IA (L. 132/2025) e ricava gli obblighi — pratiche vietate, alto rischio, trasparenza verso gli utenti, ruolo di fornitore o deployer, alfabetizzazione del personale. Usala prima di lanciare una funzione basata su IA, quando integri un modello di terzi in un prodotto, quando un cliente chiede garanzie sull'AI Act, per l'uso dell'IA nella selezione o gestione del personale, o per progetti di IA nella Pubblica Amministrazione.
---

# Conformità AI Act

> **Revisione normativa:** 2026-10-03 · **Ambito:** UE e Italia · Il calendario dell'AI Act è stato
> oggetto di proposte di rinvio (pacchetto *Digital Omnibus*): prima di indicare una scadenza
> verifica sulle fonti in `references/sources.md` se la data del regolamento è ancora quella in
> vigore.
> Questa skill struttura la valutazione; non è consulenza legale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Primo passo: che ruolo hai

Gli obblighi dipendono dal ruolo, non dalla tecnologia.

- **Fornitore (provider):** sviluppa il sistema o lo immette sul mercato con il proprio nome. Una
  software house che vende un prodotto con IA dentro è fornitore di quel sistema, anche se il modello
  sotto è di un terzo.
- **Deployer:** usa il sistema sotto la propria autorità nell'attività professionale. Il cliente che
  usa il tuo prodotto è deployer.
- Importatore e distributore, quando il sistema viene da fuori UE o passa di mano.

Chi modifica in modo sostanziale un sistema ad alto rischio, o ci mette il proprio marchio, diventa
fornitore.

## Secondo passo: in che fascia sta

1. **Vietato (art. 5).** Manipolazione subliminale, sfruttamento di vulnerabilità, social scoring,
   riconoscimento delle emozioni sul lavoro e a scuola, categorizzazione biometrica su dati sensibili,
   scraping indiscriminato di volti. Non si mitiga: si toglie.
2. **Alto rischio (art. 6, allegati I e III).** Tra i casi dell'allegato III che toccano più spesso
   una software house: selezione e gestione del personale, accesso all'istruzione, accesso a servizi
   pubblici e prestazioni, merito creditizio. Obblighi del fornitore: gestione del rischio, qualità
   dei dati, documentazione tecnica, log, supervisione umana, accuratezza e robustezza, valutazione
   di conformità, registrazione nella banca dati UE. Il deployer pubblico deve fare anche la
   valutazione d'impatto sui diritti fondamentali (art. 27).
3. **Trasparenza (art. 50).** Chatbot che dichiarano di essere IA, contenuti sintetici marcati in
   modo leggibile da macchina, deepfake etichettati.
4. **Rischio minimo.** Nessun obbligo specifico oltre all'alfabetizzazione.

I modelli per finalità generali (GPAI) hanno obblighi propri in capo a chi li sviluppa; chi li
integra ne riceve la documentazione e resta responsabile del proprio sistema.

## Calendario del regolamento

In vigore dal 1° agosto 2024. Pratiche vietate e alfabetizzazione dal 2 febbraio 2025; GPAI,
governance e sanzioni dal 2 agosto 2025; la maggior parte degli obblighi, compresi alto rischio
dell'allegato III e trasparenza, dal 2 agosto 2026; alto rischio dell'allegato I dal 2 agosto 2027.
Queste sono le date del testo originale: controlla se sono state modificate.

## Cosa aggiunge l'Italia

La L. 132/2025 designa AgID e ACN come autorità nazionali e aggiunge regole per settore: il datore
di lavoro informa i lavoratori sull'uso di sistemi di IA, i professionisti informano i clienti
quando usano IA nella prestazione, per i minori di 14 anni serve il consenso dei genitori, e la PA
usa l'IA come supporto alla decisione, che resta della persona. Per la selezione del personale
coordina con `people:hiring-and-interviewing`.

## Alfabetizzazione (art. 4)

Fornitori e deployer devono garantire un livello sufficiente di competenza sull'IA a chi la usa per
loro conto. Vale per tutti, anche per il rischio minimo, ed è già applicabile: una formazione
documentata e proporzionata al ruolo è la prova.

## Cosa restituire

1. Ruolo e fascia di rischio, con l'articolo o la voce di allegato che li determina.
2. Obblighi applicabili e da quando, con la fonte della data.
3. Interventi di prodotto (avvisi, log, supervisione umana, marcatura dei contenuti).
4. Punti incerti da portare a un legale.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Classificare un sistema senza aver stabilito chi è fornitore e chi è deployer.
- Trattare un caso dell'allegato III come rischio minimo perché "c'è un umano che decide".
- Dare per certa una scadenza senza averne verificato lo stato attuale.
- Addestrare o migliorare un modello con dati personali raccolti per un'altra finalità.
