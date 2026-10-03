---
name: privacy-and-data-protection
description: Valuta e migliora come un'azienda italiana raccoglie, usa, condivide e conserva dati personali secondo GDPR, Codice privacy (D.Lgs. 196/2003) e prassi del Garante — mappa dei trattamenti, base giuridica, informative, consenso e cookie, nomine a responsabile, diritti degli interessati, data breach, trasferimenti extra UE. Usala prima di lanciare qualsiasi cosa che tratta dati personali, quando arriva un nuovo fornitore che li tratterà, quando un interessato esercita un diritto, per marketing via email, SMS o telefono, per controlli sui dipendenti, o per prepararsi a un'ispezione.
---

# Privacy e protezione dei dati

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia e UE · Prima di rispondere su obblighi,
> termini o sanzioni controlla le fonti in `references/sources.md`: il Garante pubblica provvedimenti
> ogni settimana.
> Questa skill struttura la valutazione e indica cosa portare a un professionista; non è consulenza
> legale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Parti dal registro dei trattamenti

Non puoi valutare quello che non hai inventariato. Il registro (art. 30 GDPR) è anche il documento
che il Garante chiede per primo in un'ispezione, e l'esenzione per chi ha meno di 250 dipendenti
non vale quasi mai: cade appena il trattamento non è occasionale, e paghe e clienti non lo sono.

Per ogni trattamento:

- Quali dati, di chi, da dove arrivano.
- Per quale finalità precisa e con quale base giuridica (art. 6; art. 9 per i dati particolari).
- Dove stanno, chi vi accede, quali fornitori li ricevono e con quale nomina.
- Per quanto tempo, e cosa li cancella davvero. "Illimitato" è una non conformità, non una risposta.
- Se escono dallo Spazio economico europeo, e su quale meccanismo.

## Le regole italiane che il GDPR da solo non ti dice

- **Marketing diretto (art. 130 Codice privacy).** Email, SMS e chiamate automatizzate richiedono
  il consenso. Unica eccezione, il *soft spam*: email a un cliente, per prodotti analoghi a quelli
  già acquistati, all'indirizzo che ti ha dato in quell'occasione, con opposizione facile in ogni
  messaggio. Il telemarketing con operatore deve consultare il Registro pubblico delle opposizioni,
  che dal 2022 copre anche i cellulari.
- **Cookie e tracciamento.** Linee guida del Garante del 10 giugno 2021: lo scroll non è consenso,
  chiudere il banner con la X equivale a rifiutare, il rifiuto deve essere facile quanto
  l'accettazione, e non si ripropone il banner prima di sei mesi salvo cambi sostanziali.
- **Minori.** In Italia il consenso ai servizi della società dell'informazione vale da 14 anni
  (art. 2-quinquies Codice privacy), non da 16.
- **Dipendenti.** Videosorveglianza e strumenti da cui deriva un controllo a distanza richiedono
  accordo sindacale o autorizzazione dell'Ispettorato (art. 4 Statuto dei lavoratori); la sola
  informativa non basta. I metadati delle email aziendali vanno conservati per pochi giorni: il
  documento di indirizzo del Garante del 2024 indica 21 giorni come riferimento. Per gli
  amministratori di sistema vale il provvedimento del 27 novembre 2008 (nomina, elenco, log degli
  accessi). Su tutto il lato lavoro coordina con `people:employee-relations`.

## Scelte di progetto che evitano problemi

- **Raccogli meno.** Ogni campo è un rischio con un costo di manutenzione.
- **La finalità limita davvero.** Dati raccolti per un servizio non sono disponibili per addestrare
  un modello: è il caso in cui oggi si sbaglia più spesso. Vedi `legal-risk:eu-ai-act-compliance`.
- **Privacy by design (art. 25)** si dimostra con le scelte documentate, non con una dichiarazione.
- **Conservazione con un meccanismo che la applica.** Una policy senza job di cancellazione è
  un'intenzione.

## DPIA e DPO

La valutazione d'impatto (art. 35) è obbligatoria quando il trattamento è ad alto rischio; il
Garante ha pubblicato l'elenco italiano dei trattamenti che la richiedono sempre (tra cui
geolocalizzazione dei dipendenti, profilazione su larga scala, dati biometrici). Va fatta prima
di partire, non a sistema in produzione.

Il DPO è obbligatorio per le autorità pubbliche e per chi monitora interessati su larga scala o
tratta dati particolari su larga scala come attività principale. Una software house che gestisce
in outsourcing piattaforme per la PA spesso ricade nel secondo caso per conto del cliente: chiarisci
i ruoli prima di firmare.

## Fornitori e ruoli

Chi tratta dati per tuo conto è responsabile del trattamento e serve un atto di nomina (art. 28)
che copra istruzioni, sicurezza, sub-responsabili, cancellazione a fine rapporto, assistenza sui
diritti e sui breach. Una software house è quasi sempre responsabile per i dati dei clienti che
ospita o gestisce: deve avere un proprio modello di nomina da proporre, non subirne uno diverso
per cliente. Vedi `legal-risk:contract-review`.

**Trasferimenti extra SEE:** verso gli Stati Uniti basta il Data Privacy Framework solo se il
fornitore è certificato; altrimenti clausole contrattuali standard con valutazione d'impatto del
trasferimento.

## Diritti e data breach

Processo pronto prima della prima richiesta: canale, verifica dell'identità, ricerca del dato in
tutti i sistemi, risposta entro un mese (prorogabile di due con motivazione). La ricerca è la parte
che fallisce.

**Data breach:** notifica al Garante entro 72 ore da quando ne sei venuto a conoscenza (art. 33),
con la procedura online del Garante; comunicazione agli interessati se il rischio è elevato
(art. 34). Ogni violazione, anche non notificata, va registrata. Se l'azienda è soggetto NIS gli
stessi fatti possono far scattare la notifica al CSIRT Italia con termini più stretti: vedi
`security:incident-response`.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono le domande trattate qui,
per cosa fanno fede e cosa puoi farne. Consultale prima di rispondere su ciò che coprono e cita
quelle che hai usato. Normattiva ed EUR-Lex sono citabili; le pagine del Garante si leggono e si
citano, non si copiano.

## Never

- Raccogliere dati perché un giorno potrebbero servire.
- Usare il consenso come base giuridica quando il trattamento è necessario al contratto.
- Mandare dati a un fornitore prima della nomina a responsabile e della verifica del trasferimento.
- Installare cookie di profilazione prima della scelta dell'utente.
- Fare telemarketing senza consultare il Registro pubblico delle opposizioni.
- Caricare dati personali di produzione in un ambiente di test.
