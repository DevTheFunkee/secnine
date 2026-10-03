---
name: piattaforme-abilitanti
description: Progetta l'integrazione di un servizio con le piattaforme abilitanti nazionali — SPID e CIE per l'autenticazione, pagoPA per i pagamenti, App IO per messaggi e servizi al cittadino, PDND per lo scambio di dati tra enti, SEND per le notifiche digitali. Usala quando un servizio pubblico o un privato convenzionato deve autenticare cittadini, incassare pagamenti verso la PA, inviare comunicazioni su App IO, o consumare dati di altre amministrazioni.
---

# Piattaforme abilitanti

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia · Specifiche, SDK e procedure di
> adesione cambiano spesso: parti sempre dalla documentazione ufficiale in `references/sources.md`.
> Questa skill orienta l'architettura; non sostituisce le specifiche. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Quale piattaforma per quale problema

| Problema | Piattaforma | Cosa serve |
|---|---|---|
| Autenticare un cittadino | SPID, CIE (CieID) | Adesione come service provider, metadata, SAML2 o OpenID Connect |
| Incassare un pagamento verso un ente | pagoPA | Ente creditore aderente, posizioni debitorie, avvisi con IUV |
| Mandare un messaggio o un avviso al cittadino | App IO | Servizio registrato dall'ente, API dei messaggi |
| Leggere dati di un'altra amministrazione | PDND | E-service pubblicato dall'erogatore, accordo di fruizione, voucher |
| Notificare un atto con valore legale | SEND | Adesione dell'ente, API di invio |

Nella maggior parte dei casi l'aderente è l'**ente**; il fornitore integra per suo conto, spesso
come *partner tecnologico* o tramite un intermediario. Chiarisci all'inizio chi firma l'adesione:
è la dipendenza più lenta del progetto.

## Regole di progetto

- **Usa gli SDK e le librerie ufficiali** di Developers Italia dove esistono. Un'implementazione
  SAML scritta a mano è la fonte più comune di bocciature in collaudo e di vulnerabilità.
- **Collaudo prima della produzione.** Ogni piattaforma ha un ambiente di test o validazione
  obbligatorio; mettilo nel piano, con i suoi tempi.
- **Identità e privacy.** Gli attributi SPID richiesti devono essere i minimi necessari alla
  finalità; l'informativa lo dichiara (`legal-risk:privacy-and-data-protection`).
- **Pagamenti:** lo stato del pagamento è quello che comunica pagoPA, non quello del redirect.
  Riconcilia sulle ricevute.

## Privati

Anche un'azienda privata può offrire l'accesso con SPID o CIE, previa convenzione o tramite un
aggregatore; pagoPA e App IO restano invece servizi degli enti. Per i privati la domanda giusta è
se il volume giustifica il costo dell'adesione.

## Cosa restituire

1. Le piattaforme necessarie e chi deve aderire a ciascuna.
2. Architettura di integrazione, ambienti e collaudi previsti.
3. Dipendenze esterne con i loro tempi, in testa al piano.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande. Consultale
prima di rispondere e cita quelle usate.

## Never

- Implementare SAML o OIDC per SPID da zero quando esiste una libreria ufficiale.
- Considerare pagato un avviso pagoPA sul solo esito del redirect.
- Chiedere a SPID attributi che il servizio non usa.
- Pianificare il go-live senza il collaudo della piattaforma.
