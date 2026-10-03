---
name: incident-response
description: Gestisce un incidente di sicurezza dalla rilevazione alla chiusura — triage, contenimento, indagine, comunicazione e revisione finale — con le notifiche obbligatorie in Italia e UE (Garante entro 72 ore per i dati personali, CSIRT Italia a 24 e 72 ore per i soggetti NIS, vulnerabilità sfruttate secondo il Cyber Resilience Act). Usala quando si sospetta o si conferma una compromissione, per preparare un piano di risposta o un'esercitazione, per decidere se un evento è un incidente, o quando una violazione può far scattare obblighi di notifica.
---

# Risposta agli incidenti

> **Revisione normativa:** 2026-10-03 · **Ambito:** Italia e UE · I termini di notifica decorrono
> da quando sei venuto a conoscenza dell'evento e si misurano in ore: coinvolgi Legal & Risk appena
> possono esserci dati personali o un obbligo NIS, non a lavoro tecnico finito.
> Questa skill guida la risposta; le notifiche sono atti giuridici. Limiti d'uso: <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

## Decidi che è un incidente, e dillo

Il ritardo più caro è l'ora passata a discutere se lo sia davvero. Dichiaralo presto: chiudere un
incidente dichiarato costa poco, scoprire un'ora dopo che era reale no.

Nomina subito un **incident commander**: una persona che coordina e non fa il lavoro tecnico.
Tutti gli altri hanno un compito definito. Gli incidenti falliscono sul coordinamento molto più che
sulle capacità tecniche.

## Ordine delle operazioni

**1. Contieni prima di indagare.** Isola l'host, revoca la credenziale, disabilita l'account,
blocca il percorso. Osservare l'attaccante per capirne di più si fa solo per decisione esplicita.

**2. Preserva le evidenze mentre contieni.** Snapshot prima di ricostruire; stato volatile
(memoria, connessioni, processi) prima di spegnere. Ricostruire un host compromesso distrugge
l'unica traccia di come sono entrati.

**3. Definisci il perimetro.** Cosa è stato visto, cosa è stato preso, da quando, se è ancora in
corso. Il perimetro iniziale è quasi sempre sottostimato: cerca persistenza e movimento laterale
prima di dichiarare il contenimento.

**4. Eradica e ripristina.** Chiudi l'accesso e il percorso, poi ripristina da uno stato noto e
pulito invece di pulire sul posto. Ruota ogni credenziale raggiungibile, non solo quelle usate.

**5. Sorveglia dopo il ripristino.** I rientri sono frequenti.

## Notifiche in Italia e UE

Tieni la cronologia con l'ora in cui l'azienda è venuta a conoscenza dell'evento: è da lì che
partono tutti i termini.

| Se… | A chi | Entro |
|---|---|---|
| Sono coinvolti dati personali con rischio per le persone | Garante privacy (art. 33 GDPR) | 72 ore |
| Il rischio per le persone è elevato | Gli interessati (art. 34 GDPR) | Senza ingiustificato ritardo |
| L'azienda è soggetto NIS e l'incidente è significativo | CSIRT Italia (D.Lgs. 138/2024) | Preallarme 24 ore, notifica 72 ore, relazione finale entro un mese |
| Una vulnerabilità di un tuo prodotto è sfruttata attivamente | CSIRT designato ed ENISA (Cyber Resilience Act) | Preallarme 24 ore, secondo i termini del regolamento |
| Sei un'entità finanziaria | Autorità di settore (DORA) | Termini propri di DORA |

Sei un fornitore? Il contratto con un cliente soggetto NIS o titolare del trattamento ti obbliga
quasi sempre ad avvisarlo entro poche ore, perché lui possa rispettare i suoi termini. Quel termine
contrattuale è il tuo vero orologio. Inquadramento NIS in `legal-risk:nis2-compliance`, privacy in
`legal-risk:privacy-and-data-protection`.

## Comunicazione

Una sola cronologia come fonte di verità, con ogni voce datata e attribuita. Comunica cosa si sa,
cosa non si sa ancora e quando arriva il prossimo aggiornamento. Non speculare all'esterno su causa
o perimetro prima che siano accertati: una smentita allunga la storia e danneggia la credibilità più
dell'incidente.

## Dopo

Revisione senza colpe, centrata sul sistema: come potevamo accorgercene prima, cosa ha rallentato
il contenimento, cosa ci mancava, cosa l'ha reso possibile. Ne escono azioni con responsabile e
data; una revisione senza cambiamenti è teatro. Per i soggetti NIS la relazione finale al CSIRT
riprende questi contenuti.

## Preparazione

Il piano conta meno di averlo provato. Almeno un'esercitazione all'anno su uno scenario realistico,
compresa la notifica: chi decide fuori orario, dove sono le credenziali, chi chiama il legale, chi
compila il modulo del Garante.

## Fonti

`references/sources.md` in questa skill elenca le autorità che decidono queste domande, comprese
alcune fonti statunitensi e internazionali citate per il metodo di gestione (NIST, MITRE) e non per
gli obblighi. Consultale prima di rispondere e cita quelle usate.

## Never

- Ricostruire o cancellare un host compromesso prima di aver acquisito le evidenze.
- Far gestire la comunicazione esterna a chi conduce la risposta tecnica.
- Aspettare di conoscere la causa per avviare le notifiche con termine in ore.
- Chiudere un incidente prima di sapere come sono entrati e che il percorso è chiuso.
- Speculare su causa o attribuzione fuori dal canale di risposta mentre l'incidente è aperto.
