---
name: nis2-compliance
description: Stabilisce se un'azienda è soggetta alla NIS2 come recepita in Italia dal D.Lgs. 138/2024 e cosa comporta — registrazione sul portale ACN, misure di sicurezza di base, notifica degli incidenti al CSIRT Italia, responsabilità degli organi di amministrazione, obblighi verso la catena di fornitura. Usala quando un cliente chiede di dimostrare la conformità NIS2, per capire se la tua azienda rientra tra i soggetti essenziali o importanti, per preparare la registrazione annuale, o per impostare il piano di sicurezza su misure e notifiche NIS.
---

# Conformità NIS2

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia e UE · Le scadenze operative le fissano
> le determinazioni ACN, che cambiano più spesso del decreto: leggile in `references/sources.md`
> prima di dare una data.
> Questa skill struttura la valutazione; non è consulenza legale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Prima domanda: sei un soggetto NIS?

Tre passi, in quest'ordine:

1. **Settore.** L'attività è in un settore degli allegati del decreto? Per una software house i
   più probabili sono *gestione dei servizi TIC B2B* (fornitori di servizi gestiti e di servizi di
   sicurezza gestiti), *fornitori di servizi digitali* (marketplace, motori di ricerca, social) e
   *infrastrutture digitali* (data center, cloud, DNS).
2. **Dimensione.** Di norma sono incluse le medie e grandi imprese: almeno 50 dipendenti, oppure
   fatturato o bilancio annuo oltre 10 milioni di euro, calcolati sul gruppo secondo la
   raccomandazione UE sulle PMI. Alcuni soggetti sono inclusi a prescindere dalla dimensione
   (tra gli altri DNS, registri TLD, prestatori di servizi fiduciari, reti pubbliche di
   comunicazione).
3. **Essenziale o importante.** Dipende da settore e dimensione; cambia il regime di vigilanza e il
   tetto delle sanzioni, non la sostanza delle misure.

Se non sei soggetto, la NIS2 ti arriva lo stesso dai clienti: i soggetti NIS devono gestire il
rischio della propria catena di fornitura e lo scaricano sui contratti. Preparati alle loro
richieste con le stesse misure di base.

## Registrazione

I soggetti si registrano sulla piattaforma ACN e aggiornano i dati ogni anno nella finestra fissata
dal decreto (tra il 1° gennaio e il 28 febbraio). Serve un *punto di contatto* nominato. Dopo la
registrazione è ACN a comunicare se sei incluso nell'elenco e con quale qualifica: da quella
comunicazione partono i termini per misure e notifiche.

## Misure

L'art. 24 del decreto (art. 21 della direttiva) chiede misure proporzionate su: analisi dei rischi,
gestione degli incidenti, continuità e backup, sicurezza della catena di fornitura, sviluppo e
manutenzione sicuri, gestione delle vulnerabilità, formazione, crittografia, controllo degli
accessi e MFA. ACN ha tradotto questo elenco in *misure di base* con requisiti verificabili:
parti da quelle, non dal testo della direttiva. Per il metodo usa `security:chief-information-security-officer`
e `security:vulnerability-management`.

## Notifica degli incidenti

Per un incidente significativo, al CSIRT Italia:

- **preallarme entro 24 ore** da quando ne vieni a conoscenza;
- **notifica entro 72 ore**, con valutazione iniziale di gravità e impatto;
- **relazione finale entro un mese** dalla notifica.

Se ci sono anche dati personali coinvolti, la notifica al Garante (72 ore, GDPR) è separata e
parallela. La procedura operativa sta in `security:incident-response`.

## Responsabilità degli organi

Gli organi di amministrazione approvano le misure, ne sovrintendono l'attuazione, seguono una
formazione e rispondono delle violazioni. Non è un tema delegabile all'IT: il verbale del CdA o la
delibera dell'amministratore unico che approva il piano è un documento da avere.

## Cosa restituire

1. Esito dell'inquadramento: soggetto sì o no, settore, qualifica attesa, con il ragionamento.
2. Scadenze applicabili, ciascuna con la determinazione ACN che la fissa.
3. Gap rispetto alle misure di base, in ordine di rischio.
4. Cosa chiedere a consulente legale e a ACN quando l'inquadramento è incerto.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Concludere di non essere soggetti senza aver verificato settore e dimensione del gruppo.
- Dare una scadenza NIS senza la determinazione ACN che la fissa.
- Aspettare la causa dell'incidente per inviare il preallarme a 24 ore.
- Trattare l'approvazione delle misure come compito del solo responsabile IT.
