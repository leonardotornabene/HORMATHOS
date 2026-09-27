> **English translation; the Italian original governs** (V3-012).
> Original: `docs/g1_ratification_record.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `6a825db2e658e629bdc65b7b466aad8342cc7f5accaaa426a98ddc0f65136234`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original; numbers use English notation; link targets and paths are reproduced unchanged and resolve as they did at `5f1ec06`. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# G1 — register of the ratifications

**Status: only the technical items 17–20 and 23–26 are ratified; all the scientific
decisions remain open.** This file is the single place where the decisions are
recorded as they are taken. It is not a document of
evidence and does not duplicate its content: every row carries a label and a number,
and the authority on numbers and arguments remains the checklist of
`docs/g1_D55_proposal.md` (with `docs/g1_registry_proposal.md` for the 30 rows).

**Rule.** The technical ratifications of 4 September are applied to the branch
`g1/pre-audit`; they do not modify constants, registry, alphabet or T\*. The scientific
decisions recorded here do not apply until their amendments
are deposited. `01_MASTER_SPEC.md`, `02_DECISION_LOG.md` and the scientific values
in `config/` therefore remain intact; item 18 requires separate amendments.

**Replaces** `HEXIS_foglio_ratifica_G1.pdf` (18 August 2026, `g1/pre-audit` @
`61d6496`), archived outside the tree — sha256
`73b2afcbbb9774e228a68bf8f1de453be532757fcb02ba9aa30012cc431f39d4`.
**Its numbering cannot be transferred here: only items 1–11 coincide.** The
sheet numbers 12, 13, 14 and 15 what here is **17, 18, 19 and 21**; it leaves without
a number, in its section C, what here is **12–16**; and it does not contain at all
items **20, 22, 23, 24, 25, 26, 27** nor the **documentary scope of the alphabet**. A verdict taken
on the sheet must therefore be transcribed **by topic, never by number**. A
signable copy is regenerated at the end, with the verdicts inside, if needed.

**Language:** Italian like the sheet, because it is the surface with which you decide; the
`Dnn-A1` items that derive from it will be in English like the rest of the Decision Log.

---

## Recommended order

The technical block 17–20 and 23–26 is concluded. For what remains:

1. **Item 21 first** — it decides whether items 1–7 are taken today or after the
   linguistic supervisor. It is the only one that reorders all the others, and it costs nothing.
2. **Items 8–11** — freeze contracts and GATE-A readings, still scientific or
   coupled to the ratified content.
3. **Item 1** — with the supervisor if 21 says «before», alone if it says «after».
4. **Item 27, then 2–7** — first the URN conflict of Tacitus is settled, then
   the whole registry that contains it can be ratified.
5. **Section B** — after the freeze, at the gates that require it.

---

## A — they block the G1 freeze

| # | decision | depends on | status | verdict | date |
| --- | --- | --- | --- | --- | --- |
| 1 | Primary Greek contrast: option **A**, **B** or **route A\*** (A + conditional switch on O7, both T\* frozen) | 21 · reciprocal with 16 under A\* | OPEN | — | — |
| 2 | The registry: all 30 rows (regime, `meter`, `period`, `flags`, `source_urn`) | 21 · 27 | OPEN | — | — |
| 3 | Caesar, *De bello Gallico* — regime (proposed PROSE_CLASS) | 21 | OPEN | — | — |
| 4 | Athenaeus 12+13 — merge, **and with it the `part_order` constraint** | 21 | OPEN | — | — |
| 5 | Single books (Herodotus 1, Thucydides 1, Diodorus 11) as whole documents | 21 | OPEN | — | — |
| 6 | Vocabulary and values of the `period` field | 21 | OPEN | — | — |
| 7 | O8 and the `author_block` field | 21 | OPEN | — | — |
| 8 | GATE-A — the five declared readings | — | OPEN | — | — |
| 9 | `alphabet.json`: form · **documentary scope** · extent of the freeze · atomicity (+ `.gitignore` exception) · contract | — | OPEN | — | — |
| 10 | `t_star`: proposed signature and the two keys of `config/default.yaml` | — | OPEN | — | — |
| 11 | Semantic inventory check — what it is compared against (+ fourth expectation: scope of the alphabet) | — | OPEN | — | — |
| 21 | Touchpoint of the linguistic supervisor **before** the freeze (`D29-A1`) | — | OPEN | — | — |
| 27 | Tacitus `phi1351.phi005`: the text is the *Historiae*, but Perseus assigns phi005 to the *Annales*. **(a)** keep the upstream URN and the flag · **(b)** correct `source_urn` to phi004 · **(c)** hold the row for the linguistic supervisor (**recommended**) | 21 | OPEN | — | — |

## B — they block later gates, not the freeze

| # | decision | depends on | status | verdict | date |
| --- | --- | --- | --- | --- | --- |
| 12 | Latin family: its own of 2 or joined in one of 4 | 1 | OPEN | — | — |
| 13 | `sent_ord` rule (the ordering; the constraint is at item 4) | 4 | OPEN | — | — |
| 14 | Grid of the learning curves | 1 | OPEN | — | — |
| 15 | O4 — verse inserts in Petronius | — | OPEN | — | — |
| 16 | O7 — its resolution (G3 study on synthetic data) | 1 (profile of sizes) | OPEN | — | — |
| 22 | The Latin arm at T\* = 638: it remains an arm of the design or becomes an appendix | — | OPEN | — | — |

## C — repository and process governance

| # | decision | depends on | status | verdict | date |
| --- | --- | --- | --- | --- | --- |
| 17 | Software conventions §xiv, `--force` only pre-audit and strict re-attestation discipline | — | RATIFIED | Canonical clean and without `--force`; every substantial commit requires the gates, except a single administrative HANDOFF-only commit | 2026-09-04 |
| 18 | Route for depositing the amendments | — | RATIFIED | Separate items, each with its own impact | 2026-09-04 |
| 19 | `results/` and frozen artifacts | — | RATIFIED | `results/` stays tracked; explicit `.gitignore` exception for the future frozen artifacts | 2026-09-04 |
| 20 | Gate `g1`: mandatory coverage inventory | — | RATIFIED | The current eleven areas are normative; the two inventory files are anchored by the repository `conftest.py` | 2026-09-04 |
| 23 | Binding the audit inputs to `PROVENANCE.md` | — | RATIFIED | Canonical blocks absence or mismatch; pre-audit exposes them in the report and manifest | 2026-09-04 |
| 24 | Documentary scope of the ratification act | 18 | RATIFIED | The act that changes the scientific state updates in the same commit every pointer and derived copy still applicable | 2026-09-04 |
| 25 | Identity of the three copies of the standing instructions | — | RATIFIED | Byte-for-byte test; in `AGENTS.md` only the first line differs | 2026-09-04 |
| 26 | Authority of the canonical registry | 2 · 18 | RATIFIED | Only `config/registry_overrides.yaml`, on a clean Git commit; `_status` remains necessary but not sufficient | 2026-09-04 |

---

## Verdicts

On 4 September 2026 the owner approved the complete technical remediation,
without authorizing any scientific choice:

- **17:** the technical conventions ratified as rewritten in §xiv. The canonical run
  requires a clean commit and refuses `--force`; the pre-audit may force but declares
  the risk of a partial state. Every substantial commit requires a new run;
  only a final commit that modifies exclusively `docs/HANDOFF.md` may report
  the counts measured on its parent.
- **18:** the route of separate amendments chosen.
- **19:** `results/` stays versioned; the exception for the future frozen artifacts
  will be explicit and simultaneous with the freeze.
- **20:** the current G1 inventory is normative and the G0/G1 inventory files cannot
  be removed or unmarked while leaving the gate green.
- **23:** the existing Markdown of `PROVENANCE.md` is the anchor; no new format.
- **24:** the future scientific act must update in the same commit all the
  pointers and derived documents that it makes false; no manual count of
  occurrences constitutes proof of completeness.
- **25:** the three copies of the instructions are bound by tests.
- **26:** the canonical authority derives from the repository path and from the clean commit
  recorded in the manifest. The path is not attributed a cryptographic proof of
  human intention that it does not possess.
