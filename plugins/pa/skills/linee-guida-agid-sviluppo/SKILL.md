---
name: linee-guida-agid-sviluppo
description: Applica le regole che la PA italiana impone al software che compra o commissiona — valutazione comparativa e riuso (art. 68 CAD), rilascio in open source e publiccode.yml (art. 69), interoperabilità secondo il Modello AgID e PDND, design .italia, sviluppo sicuro. Usala quando progetti o consegni software per un ente pubblico, quando un capitolato cita le linee guida AgID, per preparare un repository a riuso su Developers Italia, o per progettare API destinate allo scambio tra amministrazioni.
---

# Linee guida AgID per lo sviluppo

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia · Le linee guida AgID hanno versioni
> numerate e periodi transitori: cita sempre la versione letta in `references/sources.md`.
> Questa skill orienta la progettazione; il capitolato di gara prevale. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Perché contano

Il CAD rende vincolanti le linee guida AgID (art. 71): un capitolato che le richiama le trasforma in
requisiti di collaudo. Ignorarle non fa perdere la gara, fa fallire il collaudo.

## Riuso e open source

- **Prima di comprare, l'ente valuta** se esiste già una soluzione a riuso o open source (art. 68
  CAD). Una soluzione nel catalogo Developers Italia è un concorrente gratuito del tuo prodotto.
- **Software commissionato dalla PA** va rilasciato con licenza aperta e pubblicato, con il file
  `publiccode.yml` che lo descrive, nel catalogo del riuso (art. 69). Il contratto deve dirlo e il
  repository deve essere pulito: niente segreti, dipendenze con licenze compatibili, documentazione
  di installazione.
- Il tuo prodotto proprietario può restare proprietario se lo vendi come tale: la distinzione tra
  personalizzazione pagata dall'ente e prodotto preesistente va scritta nell'offerta.

## Interoperabilità

Le API esposte o consumate tra amministrazioni seguono il Modello di interoperabilità (ModI): REST
documentate in OpenAPI 3, pattern di sicurezza e firma dei messaggi definiti, pubblicazione come
e-service sulla Piattaforma Digitale Nazionale Dati (PDND) con autorizzazione tramite voucher.
Progetta l'API secondo `technology:api-design`, poi verifica i pattern ModI richiesti.

## Design dei servizi

Siti e servizi al cittadino usano i modelli Designers Italia e Bootstrap Italia; per comuni e
scuole i modelli sono spesso condizione per i finanziamenti PNRR. Coordina con
`product:design-system`.

## Sicurezza

Le misure minime per le PA, le linee guida AgID sullo sviluppo sicuro e, per i servizi cloud, la
qualificazione ACN. In pratica: threat modeling a inizio progetto (`security:threat-modeling`),
review prima del rilascio (`security:security-architecture-review`), gestione delle vulnerabilità
anche dopo il collaudo.

## Cosa restituire

1. Quali linee guida si applicano al progetto e in quale versione.
2. Requisiti che diventano criteri di collaudo, con la fonte.
3. Impatti su architettura, licenza del codice e repository.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Consegnare software commissionato dalla PA senza licenza aperta e `publiccode.yml`.
- Esporre un'API tra enti fuori dal Modello di interoperabilità quando il capitolato lo richiede.
- Lasciare credenziali o dati dell'ente nel repository da pubblicare a riuso.
- Citare una linea guida senza indicarne la versione.
