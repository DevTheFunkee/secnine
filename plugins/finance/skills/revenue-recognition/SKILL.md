---
name: revenue-recognition
description: Determines when and how revenue is recognized — performance obligations, contract terms that change the answer, and the deal structures that create accounting problems. Use this to work out how a contract should be recognized, review a non-standard deal before it is signed, understand deferred revenue, or spot terms that would delay or reverse recognition.
---

# Revenue recognition

<!-- eu-it: da-localizzare -->
> **Edizione IT/UE: skill non ancora localizzata.** Il metodo vale ovunque, ma i riferimenti
> normativi qui sotto sono statunitensi e non si applicano in Italia o nell'UE. ASC 606 va sostituito da OIC 34 (o IFRS 15 per chi lo adotta).
> Per gli obblighi usa invece: OIC 34 Ricavi; IFRS 15 (Reg. UE 2016/1905).
> Non è consulenza professionale: limiti d'uso in <https://github.com/DevTheFunkee/secnine/blob/main/DISCLAIMER.md>.

Cash received is not revenue earned. The gap between them is where deals get restructured after
signature and where quarters get restated.

**This structures the question and tells you what to ask. Revenue recognition is a technical
accounting matter under standards such as ASC 606 and IFRS 15 — conclusions on a material or unusual
contract need your auditors or a qualified accountant, not a checklist.**

## The shape of the question

Recognition follows the transfer of control to the customer, worked through in five steps: identify
the contract, identify the distinct performance obligations, determine the transaction price,
allocate it across the obligations, then recognize as each is satisfied.

Most disputes happen at step two and step four. What sales sold as one thing is frequently several
obligations for accounting purposes — software plus implementation plus support — and the price has
to be allocated across them on standalone selling price, not on how the quote was written.

## Terms that change the answer

These belong in a pre-signature review, because after signature the only remedy is an amendment the
customer has no reason to agree to:

- **Acceptance clauses** — a customer right to reject can defer recognition until acceptance.
- **Termination for convenience** — a short-notice exit can shorten the contract term for accounting
  purposes, however long the stated term is.
- **Contingent or milestone fees** — variable consideration, constrained until it is probable there
  will be no significant reversal.
- **Material rights** — a renewal or upgrade priced below standalone value can itself be a
  performance obligation carved out of today's price.
- **Extended payment terms** — payment far from delivery can introduce a financing component.
- **Side letters.** Any promise made outside the contract is still part of the contract. They are the
  single most common cause of restatement, and by construction finance does not know they exist.

## Working with sales

Recognition treatment is a deal input, not a post-signature discovery. A concession that costs
nothing commercially can move revenue across a period boundary, and by the time finance sees the
signed paper the trade has already been made.

Give `revenue:chief-revenue-officer` and `revenue:pricing-and-packaging` a small set of standard
structures that recognize cleanly, and route anything outside them through review before signature —
alongside `legal-risk:contract-review`, which owns the legal exposure the same clauses create.

## Deferred revenue is an obligation

The deferred balance is work owed, not money banked. Track it by cohort and obligation so you can
answer what it is composed of and when it releases. A balance nobody can decompose is one that
surprises you.

## Sources

`references/sources.md` in this skill lists the outside authorities that settle the questions
here — what each one is authoritative for, and what you may do with it. Check them before
answering on anything they cover, and cite what you used. Most are free to read and not free
to reproduce; the use note on each is binding.

## Tooling

Subledgers that carry recognition schedules: NetSuite Advanced Revenue Management, Zuora
Revenue, Maxio, Chargebee, Stripe Revenue Recognition, and similar.

Spreadsheet schedules hold up until contracts carry multiple performance obligations or
take mid-term modifications. That is the point to move, not a revenue threshold.

## Never

- Recognize on invoice date or cash receipt as a shortcut.
- Allocate price across obligations the way the quote happened to be laid out.
- Let a side letter exist.
- Conclude a material or novel contract's treatment without your auditors.
