> **English translation; the Italian original governs** (V3-012).
> Original: `docs/audit/CHANGELOG_RIALLINEAMENTO_v2_1.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `e3974f14af668d1d3b2da7684764ba252eda408322f6c83780312f0a82579501`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original, including Italian file names; numbers use English notation. The site labels of the tables are translated as in `AUDIT_EDITS_v2_1.json`, where they were Italian. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# CHANGELOG — DOCUMENTARY REALIGNMENT v2.1 (2026-07-21)

Execution of the decisions **D40–D51** (ratified by Massimo on 2026-07-21; adoption of the files = final ratification) on the five operational documents. Every edit was applied with exact anchoring and loud failure; the complete machine-readable trace (old/new verbatim for every edit) is in `AUDIT_EDITS_v2_1.json`. The restoration of the Master Spec is documented in full in `RESTAURO_01_MASTER_SPEC.md` (D48).

**Tag legend:** R = restoration (D48); A = ratified amendment; RA = both at the same site.

## Adoption protocol in the repository (`~/Projects/hexis/docs/`)

1. **Commit 1 (declared baseline):** commit the `.md` conversions of 2026-07-21 as they are (the five files uploaded in session), with a message that declares the damage from PDF generation (D48). This preserves the verifiable starting point.
2. **Commit 2 (v2.1):** replace the five files with the versions of this delivery and commit together `RESTAURO_01_MASTER_SPEC.md`, `CHANGELOG_RIALLINEAMENTO_v2_1.md` and `AUDIT_EDITS_v2_1.json` (suggested: in `docs/` or `docs/audit/`). The `git diff` between the two commits is the independent and complete verification of every change declared here.
3. The v2.0 in PDF may be archived (e.g. `archive_v2_0_pdf/`) as a historical record; it is no longer the canonical source.

## Summary per document

**00_LEGGIMI_INDICE.md — 12 edits.** Version 2.1; new section «What changed in v2.1»; table of the documents updated (51 decisions, O7 blocking, DN-1–3); reading order D32–D51; v2.1 verification news (Greco et al. 2023); project status with v2.1 execution order and reordered gates G0→G1→G3→G2→G4→…

| # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | A | v2.1 | version header |
| 2 | A | D41 | JSD historical note |
| 3 | A | v2.1 | v2.1 section |
| 4 | A | v2.1 | Spec row |
| 5 | A | v2.1 | Spec gate row |
| 6 | A | v2.1 | Decision Log row |
| 7 | A | v2.1 | Roadmap row |
| 8 | A | v2.1 | Handoff row |
| 9 | A | v2.1 | reading order |
| 10 | A | v2.1 | foundational checks |
| 11 | A | v2.1 | v2.1 status |
| 12 | A | D44(vii)+D45+D42 | v2.1 gate block |

**01_MASTER_SPEC.md — 6 block replacements + 40 point edits.** v2.1 reissue: D48 restoration (see RESTAURO) + table of the amendments at the top + amendments D40–D51 as per the table in the document itself. Checks passed: YAML §6.3 parsed by the parser (23 `deprel_keep`, last `parataxis`, d_max 8, family [P1, P2]); final battery 11/11 (zero ghost references §6.5, zero unannotated «optional appendix», zero «min p = 0.05», zero «profiled at G0», glyphs restored, v2.1 order declared twice, v2.1 header and footer).

Blocks (pass A): | # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | R | D48 | B1 §4.1 node fields |
| 2 | R | D48 | B2 §4.1 training pass |
| 3 | RA | D48+D44+D47 | B3 §6.1 repository tree |
| 4 | RA | D48+D44 | B4 §6.2 interfaces |
| 5 | R | D48 | B5 §6.3 YAML |
| 6 | RA | D48+D44+D45 | B6 §9 DAG |

Point edits (pass B): | # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | A | v2.1 | header version |
| 2 | A | v2.1 | v2.1 summary + amendment table |
| 3 | A | v2.1 | §0.2 label dates |
| 4 | A | D46 | §0.6 ghost ref |
| 5 | RA | D48+D41 | §1.1 R1 + emphasis |
| 6 | A | D41 | §1.2 R1 row |
| 7 | A | D49+D43+D44 | §1.2 rationale |
| 8 | A | D40 | §1.3 crosswalk |
| 9 | R | D48 | §2.5 wrapped comment |
| 10 | A | D46 | §3.7 sidecar |
| 11 | R | D48 | §4.1 emphasis |
| 12 | R | D48 | §4.1 selection s* |
| 13 | A | D45 | §4.1 profiling gate |
| 14 | RA | D48+D46+D51 | §4.2 full paragraph |
| 15 | R | D48 | §4.3 emphasis + s* |
| 16 | RA | D48+D41+D49 | §4.4 full paragraph + G_own |
| 17 | R | D48 | §4.5 emphasis |
| 18 | A | D49 | §4.5 F5 curves |
| 19 | A | realignment ⑥ | §4.5 lexicon caveat |
| 20 | RA | D43 | §5.1 full rewrite |
| 21 | RA | D48+D44 | §5.2 full rewrite |
| 22 | A | realignment ⑤ | §5.3 CI semantics |
| 23 | A | D44(vii) | §5.5 freeze reposition |
| 24 | A | D42+D50+D45 | §5.6 partition + GATE-A |
| 25 | A | D43 | §5.7 sidedness + d_max |
| 26 | A | D44(iv) | §5.8 confound pointer |
| 27 | A | D49 | §5.8 claim template |
| 28 | A | D46 | §6.4 manifest policy |
| 29 | A | D44 | §7 permutation + calibration rows |
| 30 | A | D43+D44+D49+⑤ | §8 T3 |
| 31 | A | ⑥ | §8 T6 |
| 32 | A | D49 | §8 F5 |
| 33 | A | D41 | §8 R1 figure |
| 34 | A | D44(vii)+D45 | §9 order note + criteria |
| 35 | R | D48 | §10 emphasis |
| 36 | A | D43 | §10 Tier-2 limitation |
| 37 | RA | D48+D49+D44 | App B glossary |
| 38 | A | D40 | App C crosswalk |
| 39 | A | v2.1 | footer |
| 40 | A | D41 | v2.0 summary historical note |

**02_DECISION_LOG.md — 15 edits.** Version 2.1; append-only discipline: the entries D01–D39 remain intact in the text, with only the status field extended where amended (D06→D50; D18→D18-A1 via D47; D20/D21/D24→D43; D26→D46; D30→D44(vii); D32→D41; D33→D40+D43; D36→D44, frozen as a historical record with clause (i) valid; D37→D42+D50); §II-bis with **D40–D51 in full**; §III with O6 moved to G3, **O7 blocking** and O8; §IV with the deferred nodes DN-1/2/3 and their decisive gates.

| # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | A | v2.1 | — |
| 2 | A | v2.1 | — |
| 3 | A | D50 | — |
| 4 | A | D47 | — |
| 5 | A | D43 | — |
| 6 | A | D43 | — |
| 7 | A | D43 | — |
| 8 | A | D46 | — |
| 9 | A | D44 | — |
| 10 | A | D41 | — |
| 11 | A | D40 | — |
| 12 | A | D44 | — |
| 13 | A | D42 | — |
| 14 | A | D44 | — |
| 15 | A | D45 | — |

**03_ROADMAP_OPERATIVA_IT.md — 21 edits.** Version 2.1; Phase 0 without profiling (D45); **Phase 1 split into 1a/1b** with parallel acquisition clause and note on the repositioning of G2 (D44(vii)); Phase 2 with O6+O7 and «at the end: Gate G2»; Phase 3 with the note on the presentational separation G4/G5; Phase 4 with declared sidedness, author plan descriptive without α and O7 prerequisite; Phase 5 sidedness note; Phase 6 with the D42 partition and the D50 rule; Phase 7 limits updated; checklist with three new/updated items (D43, D44, D49); «decisions that define» with item 1 updated (D41) and new items 9–11; tools note (O6→G3); bibliographic register with **crosswalk note to the final numbering**, completions to entries 2, 8, 9, 10, 25 marked [P — from the final proposal; O5 verification] and **entry 26 (Greco et al. 2023) [V 2026-07-21 on a primary source in the materials]**.

| # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | A | v2.1 | header |
| 2 | A | D45 | Phase 0 closure |
| 3 | A | D45+D44(vii)+D50+D43+D51 | Phase 1 -> 1a/1b |
| 4 | A | D44+D45+D47 | Phase 2 G3+G2 |
| 5 | A | realignment ⑦ | Phase 3 note |
| 6 | A | D43 | Phase 4 minima |
| 7 | A | D43+D44+D49 | Phase 4 criterion |
| 8 | A | D43 | Phase 5 sidedness |
| 9 | A | D42+D50+D45 | Phase 6 partition |
| 10 | A | D43 | Phase 7 limits |
| 11 | A | D43 | author-plan checklist |
| 12 | A | D44+D49 | checklist new items |
| 13 | A | D41 | decisions item 1 |
| 14 | A | D42+D44+D43+D49+D50+D51 | decisions items 9-11 |
| 15 | A | D45 | tools note |
| 16 | A | D40 | register crosswalk |
| 17 | A | D40/O5 | register #2 |
| 18 | A | D40/O5 | register #8 |
| 19 | A | D40/O5 | register #9 |
| 20 | A | D40/O5 | register #10 |
| 21 | A | D40/O5 | register #25 + #26 |

**04_AI_HANDOFF_PROMPT.md — 15 edits.** Version 2.1; bootstrap with D01–D51, O7 blocking and v2.1 order; rule 2 (JSD→D41), rule 3 (O7 clause: never freeze/run confirmatory P1 inference pre-O7), rule 7 (G2 after G3), rule 10 (D46 manifest); `CLAUDE.md` template with complete enumerations and sidedness (D43), three new «Do not» (pre-O7, candidates/, representation cells) and updated freeze; review checklist with D43/D44/D49 checks and updated limits.

| # | Tag | Decision | Site |
| --- | --- | --- | --- |
| 1 | A | v2.1 | header |
| 2 | A | v2.1 | bootstrap design tag |
| 3 | A | v2.1+D44 | bootstrap authoritative docs |
| 4 | A | D41 | rule 2 JSD |
| 5 | A | D44 | rule 3 sign-flip |
| 6 | A | D44(vii) | rule 7 freeze |
| 7 | A | D46 | rule 10 manifest |
| 8 | A | v2.1 | CLAUDE.md title |
| 9 | A | v2.1+D44 | CLAUDE.md authoritative |
| 10 | A | D44(vii) | CLAUDE.md freeze |
| 11 | A | D46 | CLAUDE.md determinism |
| 12 | A | D41 | CLAUDE.md JSD |
| 13 | A | D43+D44+D47+D42 | CLAUDE.md schemes + new do-nots |
| 14 | A | D43+D44+D49 | checklist method |
| 15 | A | D43+v2.1 | checklist text |

## Correction declared during execution (to be ratified with the adoption)

In the previous audit session Claude had doubled the two-sided thresholds also for permutations with **unequal groups**. The correct rule, now written in D43 and applied everywhere: the two-sided threshold is 2× the one-sided **only if the randomization orbit contains the mirror of the sign** — always for sign-flips; for label permutations only with equal groups; with unequal groups the thresholds coincide. Claims withdrawn: 2/462 (→ 1/462, both sidednesses), 2/28 (→ 1/28 ≈ 0.036; D24 numerically unchanged), Lysias-merged 2/56 (→ **1/56 ≈ 0.018, below Holm-1**; the status without α remains), O2 fallback with 5 blocks 0.20 (→ 1/10 = 0.10). Still valid: author plan P2 two-sided 2/20 = 0.10 (equal groups) and P1-author one-sided 1/64 ≈ 0.0156. The final proposal (§6.11) declares exactly 1/2048, 1/462, 0.10 and ≈0.016 — consistent with the correct rule.

## Outside the scope of this delivery (reminder)

- **Proposal-side erratum (§6.11):** «cannot reach family significance» → «cannot reach the **joint** significance of the family» (P1-author alone has a floor of 0.0156 < 0.025). To be integrated into the E1–E20 pass on the docx of the proposal, which remains a separate deliverable.
- **ASSUMPTIONS.md §B3:** the full text of the D18-A1 proposal must be completed from that file (outside the five documents) at the Phase 2 touchpoint.
