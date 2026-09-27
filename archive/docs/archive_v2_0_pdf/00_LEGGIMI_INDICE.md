> **English translation; the Italian original governs** (V3-012).
> Original: `docs/archive_v2_0_pdf/00_LEGGIMI_INDICE.pdf` at commit `5f1ec06` (tag `archive/pre-realign`), a PDF of 3 pages kept at this path until V3-012; SHA-256 `9bee6b2d7568e8c1a2f65e2c758715928df046662833a356ca54b7585524a422`.
> Translated on 2026-09-27 from the text of the PDF. Headings, table and lists are rebuilt from that text, with the emphasis of the later Markdown version of the same index where the wording coincides; the running page footer identifying HEXIS, the operational package index and its page number is omitted. Values and identifiers follow the original; numbers use English notation. The informal second person of the original, addressed to the author, is kept. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# PROJECT HEXIS — INDEX OF THE OPERATIONAL PACKAGE

Hexameter Information Signature — Morphosyntactic organization under metrical constraint, measured with a single instrument: the MDL context tree à la Rissanen. Version 2.0 — 6 July 2026. It replaces in full v1.0 (5 July 2026), kept in `archive_v1/`.

## What changed in v2.0 (in one sentence)

The project was consolidated around **a single statistical instrument**: the battery of separate measures of v1.0 (per-chunk entropy, confirmatory JSD, conditional entropy, mutual information with shuffle baseline) is retired as confirmatory apparatus, because those quantities are *smoothed truncations of the context tree itself*; they remain as internal diagnostics. The hypotheses become **three readings of a single model**: root (distributional), context gain (sequential, statistic P2), inter-regime transfer (predictive, statistic P1). The JSD survives as an optional appendix. Governing decisions: **D32–D39** in the Decision Log. The change happened **before any computation on the real data**, and we will declare it in the preprint.

## The five documents

| File | Language | Content | When to use it |
| --- | --- | --- | --- |
| `00_LEGGIMI_INDICE.md` | IT | This index | Now |
| `01_MASTER_SPEC.md` | EN | **The central document (v2.0):** verified corpus facts, pipeline, alphabet, the complete algorithm of the context tree with normative pseudocode, the fitting protocols (reference / regime LODO / label-free pooled LODO), the statistics P1/P2/S1/R1/L1, exact inference at the document level, software architecture, test suite with analytical truths, tables/figures, gates G0–G7 | To attach in every AI session |
| `02_DECISION_LOG.md` | EN | 39 decisions: D01–D31 reported with updated status (some superseded by D32), the new D32–D39 in full, open items O1–O6 | Every time something must change: it is amended here, never silently |
| `03_ROADMAP_OPERATIVA_IT.md` | IT | Roadmap v2.0: 13 nominal weeks within your window of 12–15, with the context tree **brought forward to Phase 2** (the greatest risk is faced immediately); acceptance criteria, comprehension checklist, template prompts; in the appendix the **COMPLETE BIBLIOGRAPHIC REGISTER** (all the sources: the 11 of the proposal, Chomsky, Galves 2012, Chen 2024, the VLMC foundations, the data resources — with verification status and role in the preprint) | Your daily guide; the register serves Phase 7 |
| `04_AI_HANDOFF_PROMPT.md` | EN | Bootstrap prompt v2.0 (with the rules of the single-instrument design), `CLAUDE.md` template, session template, review checklist | At the start of every AI session |

## Recommended reading order

1. This index.

2. `03_ROADMAP_OPERATIVA_IT.md` in full, including the section "The decisions that define the project" and the bibliographic appendix.

3. `01_MASTER_SPEC.md`: §1 (the three readings and the statistics P1/P2), §2 (corpus facts), §4 (the instrument), §9 (gates). The rest phase by phase.

4. `02_DECISION_LOG.md`: read D32–D39 in full; skim the others.

## The verification findings that remain foundational (unchanged from v1.0)

1. The Greek treebank contains **12 tragedies** (Aeschylus ×7, Sophocles ×5) and much post-classical prose → multi-regime design, with tragedy as a test of specificity.

2. The Latin treebank also contains Jerome (Vulgate, excluded), Propertius, Phaedrus, Petronius, Suetonius, Augustus; **Caesar is absent**.

3. Current release **UD v2.18**; licence **CC BY-NC-SA 2.5** (no redistribution of the data in the repository). Verification news of v2.0 (6 July 2026): citations **Galves et al. 2012** and **Chen et al. 2024** verified on the primary source and entered in the register with an obligation of differentiation in the related work.

## Golden rule of the project (unchanged)

No silent change. Every change to methodology, alphabet, parameters or protocols goes through an explicit amendment to `02_DECISION_LOG.md`. The AIs are bound to this rule by the file `04_AI_HANDOFF_PROMPT.md`.

## Project status

- [x] Research proposal (starting document)
- [x] Verification of corpus facts on primary sources (5 Jul 2026)
- [x] Operational package v1.0 (5 Jul 2026, archived)
- [x] Restructuring to a single instrument + package v2.0 (6 Jul 2026, this one)
- [ ] Gate G0: environment + non-tree tests green + fit cost profiling
- [ ] Gate G1: audit → registry, alphabet and T* FROZEN
- [ ] Gate G2: confirmatory plan frozen (OSF optional)
- [ ] Gate G3: context tree validated on the four analytical processes
- [ ] Gate G4: reference models + descriptive readings
- [ ] Gate G5: confirmatory inference (P1, P2; S1)
- [ ] Gate G6: Latin + paired subsamples
- [ ] Gate G7: sensitivity plan (13 cells) → writing
- [ ] Preprint on arXiv (cs.CL)
