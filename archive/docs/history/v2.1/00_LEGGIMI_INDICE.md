> **English translation; the Italian original governs** (V3-012).
> Original: `docs/history/v2.1/00_LEGGIMI_INDICE.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `f144ec184836a84bdaa67648df4bc16032287e8d2b217ff419dee600b2e85020`; the same bytes are listed in this folder's `SHA256SUMS.json`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original, including Italian file names; numbers use English notation. The informal second person of the original, addressed to the author, is kept. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# PROJECT HEXIS — INDEX OF THE OPERATIONAL PACKAGE

**Hexameter Information Signature** — Morphosyntactic organization under metrical constraint, measured with a single instrument: the MDL context tree à la Rissanen. **Version 2.1 — 21 July 2026.** It replaces v2.0 (6 July 2026); v1.0 (5 July 2026) is superseded and is not deposited in this repository (O9, resolved 13 August 2026).

## What changed in v2.0 (in one sentence)

The project was consolidated around **a single statistical instrument**: the battery of separate measures of v1.0 (per-chunk entropy, confirmatory JSD, conditional entropy, mutual information with shuffle baseline) is retired as confirmatory apparatus, because those quantities are *smoothed truncations of the context tree itself*; they remain as internal diagnostics. The hypotheses become **three readings of a single model**: root (distributional), context gain (sequential, statistic P2), inter-regime transfer (predictive, statistic P1). The JSD survives as an optional appendix (v2.1: raised to a planned descriptive reading, D41). Governing decisions: **D32–D39** in the Decision Log. The change happened **before any computation on the real data**, and we will declare it in the preprint.

## What changed in v2.1 (21 July 2026)

Synchronization of the operational package with the **final proposal** and closure of the procedural nodes; all pre-data decisions (**D40–D51** in the Decision Log): binding crosswalk between the hypotheses of the final proposal and the statistics (H1 = P2, H2 = P1 + S1, H3 = L1; distributional premise = root + R1; D40, verified on the final text); the JSD (R1) becomes a planned descriptive distributional reading, without α or test, with a caveat of dependence on size (D41); the sensitivity plan is partitioned into parametric robustness and analyses of representation (D42); every exact threshold declares its own sidedness and the author plan becomes descriptive without α (D43); the validity of the sign-flip of P1 is an **open and blocking question** (O7), to be resolved with a calibration study on synthetic data — for this reason **Gate G2 is repositioned after G3** (D44(vii); v2.1 order: G0 → G1 → G3 → G2 → G4 → G5 → G6 → G7; invariant intact: before G2 only synthetic data, first real fits at G4); G0 no longer requires the profiling (O6 → G3) and the acquisition of the treebanks can proceed in parallel with G0 (D45); manifest policy clarified — one central manifest per run plus a minimal sidecar per artifact (D46); `hexis_ctree` v0.1.0 in quarantine as a non-canonical candidate, with the amendment D18-A1 deposited as a proposal (D47); the Master Spec is reissued with the documented restoration of the normative blocks damaged during PDF generation (D48; complete before/after table in `RESTAURO_01_MASTER_SPEC.md`); new descriptive reading `G_own` to disambiguate the seat of the signature (D49); GATE-A × C0 rule: the primary configuration is not duplicated (D50); scope of T* restricted to the primary contrast, with the power cost of the uniform size declared (D51). Three nodes remain deliberately deferred (DN-1/2/3, decisive at G2). Bibliographic register: crosswalk with the final numbering and entry 26 (Greco et al. 2023) added and verified on the primary source.

## The five documents

| File | Language | Content | When to use it |
| --- | --- | --- | --- |
| `00_LEGGIMI_INDICE.md` | IT | This index | Now |
| `01_MASTER_SPEC.md` | EN | **The central document (v2.1, with the table of amendments at the top):** verified corpus facts, pipeline, alphabet, the complete algorithm of the context tree with normative pseudocode, the fitting protocols (reference / regime LODO / label-free pooled LODO), the statistics P1/P2/S1/R1/L1, exact inference at the document level, software architecture, test suite with analytical truths, tables/figures, gates G0–G7 (v2.1 execution order) | To attach in every AI session |
| `02_DECISION_LOG.md` | EN | 54 decisions: D01–D31 with updated status, D32–D39 (v2) in full, **D40–D51 (v2.1, synchronization with the final proposal)** in full, **D52–D54 (post-v2.1 ratification)** in full; open items O1–O8 (**O7 blocking for G2/G5**), with O9 resolved; deferred nodes DN-1–DN-3 | Every time something must change: it is amended here, never silently |
| `03_ROADMAP_OPERATIVA_IT.md` | IT | Roadmap v2.1: 13 nominal weeks within your window of 12–15, with the context tree **brought forward to Phase 2** and Phase 1 split into **1a** (non-tree pipeline → G0) and **1b** (audit → G1; acquisition in parallel with G0, D45); acceptance criteria aligned to the v2.1 order of the gates; comprehension checklist, template prompts; in the appendix the **COMPLETE BIBLIOGRAPHIC REGISTER** (the sources of the proposal with crosswalk to the final numbering, Chomsky, Galves 2012, Chen 2024, the VLMC foundations, the data resources, and Greco et al. 2023 added in v2.1 — with verification status and role in the preprint) | Your daily guide; the register serves Phase 7 |
| `04_AI_HANDOFF_PROMPT.md` | EN | Bootstrap prompt v2.1 (rules of the single-instrument design + O7/D44 discipline), `CLAUDE.md` template, session template, review checklist | At the start of every AI session |

## Operational and working documents (non-normative)

The five documents above are the normative v2.1 package and remain five. These
are not, but an agent that does not know them works in the dark.

| File | Content | Status |
| --- | --- | --- |
| `HANDOFF.md` | Attestation of the gates: commands, counts, commits on which they were measured | **Single seat of the evidence**; do not duplicate the counts elsewhere |
| `implementation/specs/` | Ratified implementation contracts — the signatures left free by the Spec (D54(v)) | Binding: `2026-08-13-g0-api-contract.md` carries obligations that block the G1 freeze |
| `probe_conllu.md` | Exploratory probe on the `.conllu` files | Descriptive |
| `g1_D55_proposal.md` | Amendment D55 + the checklist of the 27 G1 ratifications | **Scientific content PROPOSED — applied to nothing**; only the technical items 17–20 and 23–26 (§xiv) are ratified and applied to the branch on 4 Sep 2026 |
| `g1_registry_proposal.md` / `.yaml` | The 30 rows of the registry, with the evidence per row | **PROPOSED** (`_status: PROPOSED`: it does not produce a canonical audit) |
| `g1_ratification_record.md` | The register where the verdicts are deposited one at a time | Open: technical items 17–20 and 23–26 ratified; no scientific item decided |
| `audit/` | Pre-application record of amendments already executed | ARCHIVED — do not reapply |

## Recommended reading order

1. This index.

2. `03_ROADMAP_OPERATIVA_IT.md` in full, including the section "The decisions that define the project" and the bibliographic appendix.

3. `01_MASTER_SPEC.md`: §1 (the three readings and the statistics P1/P2), §2 (corpus facts), §4 (the instrument), §9 (gates). The rest phase by phase.

4. `02_DECISION_LOG.md`: read D32–D54 in full; skim the others.

## The verification findings that remain foundational (unchanged from v1.0)

1. The Greek treebank contains **12 tragedies** (Aeschylus ×7, Sophocles ×5) and much post-classical prose → multi-regime design, with tragedy as a test of specificity.

2. The Latin treebank also contains Jerome (Vulgate, excluded), Propertius, Phaedrus, Petronius, Suetonius, Augustus; **Caesar is absent**.

3. Current release **UD v2.18**; licence **CC BY-NC-SA 2.5** (no redistribution of the data in the repository). Verification news of v2.0 (6 July 2026): citations **Galves et al. 2012** and **Chen et al. 2024** verified on the primary source and entered in the register with an obligation of differentiation in the related work. Verification news of v2.1 (21 July 2026): **Greco et al. 2023** verified on the primary source in the project materials and added to the register (entry 26); complete correspondence between register and bibliography of the final proposal verified on the text.

**Warning (17 August 2026) — a pointer, not an amendment.** The G1
enumeration of the data pinned at r2.18 contradicts points 1 and 2 above: the release contains
**6 tragedies** (Sophocles ×5, Aeschylus ×1), **3** authors of post-classical prose, and
**Caesar is present** (`phi0448.phi001`, *De bello Gallico*). Complete analysis,
both options and every recomputed constant: `g1_D55_proposal.md` — **PROPOSED,
applied to nothing**. Until it is ratified, points 1 and 2 remain the text in
force: treat them as the binding plan, never as a description of this
corpus, and do not replace them silently.

## Golden rule of the project (unchanged)

No silent change. Every change to methodology, alphabet, parameters or protocols goes through an explicit amendment to `02_DECISION_LOG.md`. The AIs are bound to this rule by the file `04_AI_HANDOFF_PROMPT.md`.

## Project status

- [x] Research proposal (starting document)

- [x] Verification of corpus facts on primary sources (5 Jul 2026)

- [x] Operational package v1.0 (5 Jul 2026, superseded; not deposited in this repository, O9)

- [x] Restructuring to a single instrument + package v2.0 (6 Jul 2026)

- [x] **Synchronization with the final proposal + v2.1 realignment (21 Jul 2026, this one)**

**v2.1 execution order (D44(vii)): G0 → G1 → G3 → G2 → G4 → G5 → G6 → G7.**

- [x] Gate G0: closed on 14 Aug 2026 after pre-merge review — registry contract realigned; G0 set green with real assertions + deterministic infrastructure verified (profiling → G3; D45). Attestation (commands, counts, commits): `docs/HANDOFF.md`

- [ ] Gate G1: audit → registry, alphabet and T* FROZEN (with O2/O8 resolved)

- [ ] Gate G3: context tree validated on the four analytical processes + O6 profiling + O7 null calibration study

- [ ] Gate G2: confirmatory plan frozen (OSF optional; requires O7 resolved)

- [ ] Gate G4: reference models + descriptive readings

- [ ] Gate G5: confirmatory inference (P1, P2; S1) — requires O7 resolved

- [ ] Gate G6: Latin + paired subsamples

- [ ] Gate G7: sensitivity plan (13 cells, D42 partition) → writing

- [ ] Preprint on arXiv (cs.CL)
