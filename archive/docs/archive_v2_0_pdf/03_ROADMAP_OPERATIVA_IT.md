> **English translation; the Italian original governs** (V3-012).
> Original: `docs/archive_v2_0_pdf/03_ROADMAP_OPERATIVA_IT.pdf` at commit `5f1ec06` (tag `archive/pre-realign`), a PDF of 7 pages kept at this path until V3-012; SHA-256 `0dde74cebb3fe7603a6e28c26381760039d098d2bd39afe2bea688961a5aec18`.
> Translated on 2026-09-27 from the text of the PDF. Headings and lists are rebuilt from that text, with the emphasis of the later Markdown version of the same roadmap where the wording coincides; the running page footer identifying HEXIS, the operational roadmap and its page number is omitted. Values and identifiers follow the original, including Italian file names; numbers use English notation, and the original's own decimal points (e.g. `2.000` bits, `0.7219`) are kept. The informal second person of the original, addressed to the author, is kept. The prompts marked (EN) were already in English and are unchanged. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# PROJECT HEXIS — OPERATIONAL ROADMAP

From day zero to the preprint, v2.0 single-instrument architecture (context tree à la Rissanen). Version 2.0 — 6 July 2026. It replaces v1.0 (archived in `archive_v1/`). Addressee: you. Language: Italian. Binding technical document: `01_MASTER_SPEC.md` v2.0 (cited as §N); decisions: `02_DECISION_LOG.md` v2.0 (D01–D39).

## Premise 1: the "guided hybrid" working model (unchanged)

You remain the methodological authority; the AI is the engineer. **You understand** (without having to be able to program it): entropy and entropy rate; the MDL principle and the quantity Δ(s); why the primary quantity is the held-out cross-entropy; why the permutation is done at the document level; why the P2 scores must be built "blind" to the labels; what the results do not demonstrate. **Delegate to the AI**: code, tests, plots, debugging. **You always verify**: every number must declare data, parameters, commit and seed (manifest).

## Premise 2: time

You declared 12–15 weeks, while asking to optimize for quality and not for the calendar. The nominal plan is **13 weeks** at ~10 h/week (≈ 117–133 h in total); weeks 14–15 are a margin for the unexpected. The greatest risk of the project (the correctness of the context tree) has been **brought forward to Phase 2**: if something must break, it breaks early, when it costs little. If the time lengthens, Phase 7 (writing) lengthens, never the validation.

## Ritual of every session (10 minutes that save hours)

1. Reread the acceptance criterion of the current phase.
2. New AI session: paste the bootstrap (`04_AI_HANDOFF_PROMPT.md`) + attach Spec and Decision Log.
3. Declare: phase, task, "definition of done".
4. End of session: tests written and green? Manifest generated? If not, it is not finished.

## PHASE 0 — Environment on macOS (week 1, 6–10 h)

**Goal:** Mac ready: modern Python, versioning, Claude Code. No analysis. **Steps:** (1) Terminal; (2) `xcode-select --install`; (3) Homebrew from the official site https://brew.sh (on Apple Silicon: add `eval "$(/opt/homebrew/bin/brew shellenv)"` to the profile); (4) `brew install git` and `brew install --cask visual-studio-code`; (5) uv from the official site https://docs.astral.sh/uv, then `uv python install 3.12`; (6) **Claude Code** from the official guide **https://code.claude.com/docs/en/setup** (native installer recommended on Mac, no Node required; verify with `claude doctor`; requires a Pro/Max plan or an API key) [verified 2026-07-05]; (7) GitHub account + private repo `hexis`; (8) `git config --global user.name/email`. **Deliverable:** `git --version`, `uv --version`, `claude doctor`, `code --version` respond without errors. **Template prompt (EN):**

Read `01_MASTER_SPEC.md` §3.1 and §6.1. Initialize the `hexis` skeleton exactly per §6.1: pyproject (Python 3.12, deps §6.3), `src/hexis` stubs with the §6.2 signatures (type hints, docstrings, `raise NotImplementedError`), `tests/`, `.gitignore` (ignore `data/raw/`), `config/default.yaml` verbatim from §6.3. No logic yet. Run `uv run pytest` to confirm collection.

**Phase closure:** preliminary profiling of the cost of a synthetic fit (for item O6) → **Gate G0** together with the non-tree tests of Phase 1.

## PHASE 1 — Data pipeline + corpus audit → Gate G1 (weeks 2–3, ~18–20 h)

**Goal:** download the treebanks (v2.18, §2.5, with SHA-256 and commit in PROVENANCE.md), read them, produce the audit that **freezes alphabet, registry and T***. **What you learn:** the CoNLL-U format; the Latin multiword tokens (que/ue) and why they are expanded; the UPOS+DEPREL alphabet as a total function (§3.4); GATE-A/GATE-B; what T* is and why it is needed (§4.2). **What the AI does:** `conllu_reader`, `registry`, `alphabet`, `sequences`, `blocks` + tests (§7); `run_audit` → `audit_report.md`. **Human decisions:** you compile `config/registry_overrides.yaml` mapping every `sent_id` prefix to (author, work, regime) against the verified tables of §2.3; you resolve the duplicate *Hymn to Demeter* (O2); you check GATE-A (e.g. vocatives > 2%?) and GATE-B; you verify the verse inserts of Petronius (O4); you take note of the computed T* (binding expectation: "HEX minus Iliad"). **Acceptance criterion (G1):** no unassigned sentence; gates resolved; `alphabet.json`, registry and T* frozen; all the non-tree tests green (G0 included). **Touchpoint with the linguistic supervisor. Immediately after G1: Gate G2** — freeze of the confirmatory plan (§4.4/§5; hash of the plan recorded; OSF deposit optional). From here on, before touching real data with a model, the plan is closed; every change goes through the Decision Log. **Template prompt (EN):**

Implement `conllu_reader.py` per §3.2 and `alphabet.py` per §3.4 (TOTAL function; order of operations normative), tests first (§7, incl. a synthetic CoNLL-U fixture with one MWT range and one empty node). Then `run_audit.py` producing `audit_report.md` with the contingency tables, GATE-A/B evaluations, per-regime restricted-position fractions (D35), and the T* computation per §4.2. Do not freeze anything — I review before G1.

## PHASE 2 — THE CORE: context tree, theory + implementation + validation → Gate G3 (weeks 4–7, ~30–35 h)

It is the pivotal phase, brought forward with respect to v1: the project now is this instrument. **What you learn (indispensable, to be truly mastered):** - entropy rate; why the conditional entropy at fixed order is not enough; - MDL: a longer context is used only if it pays; Δ(s) = L_par − L_self; why prequential coding already includes the cost of the model (no separate penalty); - the monotone-stop selection rule; the role of β, k_min, γ, d_max; - why the primary quantity is the held-out CE and not h_online (D19/D32); - **Task T5.1:** complete reading of Schürmann & Grassberger 1996 §V.A–B (arXiv:cond-mat/0203436), noting in the Decision Log (possible D18-A1) every difference between the published formulas and the defaults of the Spec. **What the AI does:** it implements `model/context_tree.py` exactly per §4.1–4.3 (normative pseudocode), `model/diagnostics.py` (identity of the "slices": root = smoothed unigram; depth-1 nodes = smoothed bigrams), and the tests: the **four analytical processes** (§4.7: uniform → 2.000 bits; period-3 cycle → CE < 0.02; Markov P(stay)=0.8 → 0.7219; order-2 XOR ε=0.1 → 0.4690 against ≈1.0 of order 1), slice tests, fallback, never-seen symbols. **Acceptance criterion (G3):** all the tests listed in §7 for G3 green; T5.1 completed and logged. **Touchpoint with the mathematical supervisor.** No real data has yet been touched by a model. **Template prompt (EN):**

Implement `model/context_tree.py` per §4.1–§4.3 exactly: reversed-context trie, prequential add-β predictor, predict-then-update with PRE-update counts, Δ(s) = L_par − L_self, monotone-stop selection with k_min/γ, d_max, frozen-tree `evaluate()` with ancestor fallback and per-position records. Write `tests/test_context_tree.py` and `tests/test_tree_slices.py` FIRST with the §4.7 targets and tolerances. Do not touch real data until all pass. Explain in comments why the sequential code length already includes the model cost.

## PHASE 3 — Reference models and descriptive readings → Gate G4 (week 8, ~10 h)

**Goal:** first fits on the real data (post-freeze): one reference model per regime (protocol a, §4.2); §4.6 diagnostics green on the real fits; descriptive readings: root distributions and rank–frequency (F1), gain-vs-context and depth curves (F5–F6, via held-out protocols), CE profiles in the blocks for the Iliad and Herodotus (F7), h_online (one row per regime, SG96 comparability), and the **lexicon of the contexts** (D38: top-20 per regime by Δ(s), T6/F9) — the interpretable output for the linguist reader. **Criterion (G4):** diagnostics green; figures/tables with manifest; no confirmatory statistics yet.

## PHASE 4 — Confirmatory inference → Gate G5 (weeks 9–10, ~15 h)

**Goal:** P1 and P2 (plus secondary S1). **What you learn:** why the P2 scores are **label-free** (protocol c: pooled LODO models that never consult the labels → the exact permutation on the fixed scores is valid under H0; D36 — it corrects a subtle defect of v1); why P1 uses the sign-flip (symmetry of ΔCE under H0 with T*-matching); the **position restriction** available_past ≥ 4 (D35: the segmentation into sentences is editorial; without restriction the gain would confound organization and sentence length); Holm on the family {P1, P2} (thresholds 0.025/0.05; reachable minima 1/2048 and 1/462 — declared). **What the AI does:** `protocols/sampling.py`, `protocols/scores.py` (delta_ce_scores; pooled_scores with mandatory label-invariance test), `stats/permutation.py` (exact enumerations), hierarchical bootstrap, `run_confirmatory` → T3, T5, F2–F4 (+ learning curves F8). **Criterion (G5):** §7 tests green (including the byte-identical label-free one); results with exact Tier-1 and Tier-2 p-values (author plan: minimum 0.05, declared), effects in bits, bootstrap CIs; per-document dot plot as primary display.

## PHASE 5 — Latin + paired Greek subsamples → Gate G6 (week 11, ~8–10 h)

**Goal:** L1. Latin P1 (exact sign-flip 2^8 = 256) and Latin P2 (exact permutation C(8,2) = 28 → qualitative by construction, no α); d_max = 6; sensitivity without Petronius and without the Res Gestae; **B = 100 Greek subsamples** paired to the Latin sizes, with percentile localization of the Latin values (it answers: do the Greek–Latin differences exceed the effect of size alone?).

## PHASE 6 — Sensitivity plan → Gate G7 (week 12, ~8–10 h)

**Goal:** stability of the conclusions over the **13 cells** of D37: factorial block {alphabet-policy × boundary} = 6 cells with complete inference (S = 10; C0 at S = 20) + OAT block {β ∈ {1/|A|, 0.25, 1.0}, d_max ∈ {6, 12}, argmax, unrestricted gain} = 7 cells at point estimate. Budget ≈ 3–5 machine hours (confirmed by the G0 profiling, O6). **Claim discipline:** a conclusion is declared only if stable in sign over all the 13 cells; the instability is itself a result (T4/F10). The **UPOS-only** arm is inside the factorial block and cannot be given up (D31).

## PHASE 7 — Preprint (weeks 13–15, ~20–25 h)

**Goal:** an arXiv cs.CL preprint that stands up to a computational linguist, an information theorist and an engineer. **Structure → contents (Spec §10):** Introduction (framing by regimes; question = predictive organization under constraint); Related work in the three strands with **mandatory differentiations** from Galves et al. 2012 and Chen et al. 2024 (D39; erratum E8 on the novelty); Corpus (T1, confounders §5.8); Methods (§3–§5, algorithm §4.1, SG96 correspondence note, **paragraph on the evolution of the design**: pre-data consolidation, D32–D36); Results (descriptive readings, then confirmatory, then tragedy specificity, Latin, robustness; confirmatory/exploratory rigorously separated; negative/unstable results reported); Discussion (what the *seat* of the signature authorizes: root / gain / transfer; Anderson only conceptual); Limitations (author plan 0.05; confounders; **misspecification anchored to Chomsky 1956**: the instrument is a universal coding device, no claim that language is a finite-memory source); Future developments (proposal §10; verse boundaries D11; CTW comparator). **Sources:** all and only those of the Bibliographic register (appendix below), after the O5 completion pass. **Touchpoint with both supervisors** before submission (D29).

## Personal comprehension checklist (to tick before the preprint)

You can explain aloud, without notes: - [ ] entropy, entropy rate, cross-entropy: what they measure and in what unit; - [ ] MDL and Δ(s); why prequential coding includes the cost of the model; - [ ] how the tree selects the depth (monotone-stop) and what β, k_min, γ, d_max do; - [ ] why the primary quantity is the held-out CE and not the in-sample estimate; - [ ] why the T* matching is necessary; - [ ] why the permutation is done per document (exchangeability) and why the author plan has a minimum of 0.05; - [ ] why the P2 scores are built without consulting the labels (validity of the exact test); - [ ] why the gain is computed only on positions with available context ≥ 4; - [ ] the root and the depth-1 nodes as "smoothed slices" of the classical measures (diagnostic, not result); - [ ] what the results do NOT demonstrate: no metrical causality; no claim of finite memory of language (Chomsky 1956 as a conceptual limit).

## The decisions that define the project (summary in Italian)

*[Translator's note: the summary was written in Italian; it is given here in English.]*

1. **D32 — Single instrument.** A single model (MDL context tree); the low-order measures are its smoothed truncations: diagnostics, not results; the JSD remains as an optional appendix. Decided by you, pre-data: no confirmatory analysis had touched the real data (we will declare it in the preprint).
2. **D21 + D36 — Permutation per document and label-free scores.** The most important statistical correction (documents, not chunks) plus the v2 correction: the permuted scores must be built blind to the labels — v1 had a subtle defect here, now corrected and declared.
3. **D19/D20 — Held-out + T*.** Inference only on data never seen by the model, at equal training size.
4. **D33 — Family {P1, P2}.** Only two confirmatory statistics: transfer and context gain. Less multiplicity correction, more power; the depth (S1) is secondary because it is more sensitive to the parameters.
5. **D35 — Position restriction.** The gain is measured only where the context is available: the segmentation into sentences is editorial and must not confound the measure.
6. **D04 — Five regimes.** Tragedy as a test of specificity (signature of the hexameter or of verse?); classical vs post-classical prose separated in Greek.
7. **D31 — UPOS-only arm.** DEPRELs are noisier in poetry: everything is replicated on the alphabet of the UPOS alone; with a single instrument this check weighs even more.
8. **D06/GATE-A, D18/T5.1.** Alert threshold on the annotation discards; row-by-row audit of the correspondence with Schürmann & Grassberger.

## Note on tools

The whole analysis runs on a laptop: single fit ≈ 1–3 s (to be profiled at G0), complete sensitivity plan ≈ 3–5 hours. Claude Code (app or VS Code extension) works directly on the repository, showing the diffs before accepting them.

# APPENDIX — COMPLETE BIBLIOGRAPHIC REGISTER (D39)

All the sources of the project, in one place. Status legend: **[V]** = verified in session on the primary source (with date); **[P]** = provided by the proposal with a primary link, details to be completed; **[S]** = canonical reference, standard details to be rechecked; **[T]** = to be verified. Rule: before submission, completion pass **O5** on every non-[V] entry. Nothing is cited in the preprint unless it is in this register.

## A. Sources of the proposal (original numbering)

1. **Shannon, C. E. (1948).** "A Mathematical Theory of Communication". *Bell System Technical Journal* 27(3): 379–423; 27(4): 623–656. [S] URL of the proposal: people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf — Role: founding framework (Introduction; symbolic sources).
2. **Mansilla, R. & Bush, E.** "Increase of Complexity from Classical Greek to Latin Poetry". *Complex Systems* (volume/pages to be completed) [P/T]. URL: content.wolfram.com/sites/13/2023/02/14-3-1.pdf — Role: metrical-prosodic precedent on the hexameter; related work strand (i); differentiation: prosodic vs morphosyntactic alphabet.
3. **Universal Dependencies** (site; release **v2.18** and treebank pages) [V 2026-07-05]. URL: universaldependencies.org — Role: data source and framework.
4. **de Marneffe, M.-C., Manning, C. D., Nivre, J., Zeman, D. (2021).** "Universal Dependencies". *Computational Linguistics* 47(2): 255–308. [S] URL: direct.mit.edu/coli/article/47/2/255/98516 — Role: annotation framework (Corpus/Methods).
5. **Schürmann, T. & Grassberger, P. (1996).** "Entropy estimation of symbol sequences". *Chaos* 6(3): 414–427; arXiv:cond-mat/0203436. [V, design session] — Role: **operational authority** of the method (§4.1; Task T5.1).
6. **Montemurro, M. A. & Zanette, D. H. (2011).** "Universal Entropy of Word Ordering Across Linguistic Families". *PLoS ONE* 6(5): e19875. [S] — Role: related work (i), entropy of word order (use of Lempel–Ziv).
7. **Lin, J. (1991).** "Divergence measures based on the Shannon entropy". *IEEE Transactions on Information Theory* 37(1): 145–151. [S] — Role: definition of the JSD (appendix R1).
8. **Šeļa, A. & Gronas, M.** "Measuring Rhythm Regularity in Verse: Entropy of Inter-Stress Intervals". *CEUR Workshop Proceedings* Vol-3290 (venue of the volume to be verified, probably CHR 2022) [P/T]. URL: ceur-ws.org/Vol-3290/short_paper5417.pdf — Role: related work (i), rhythmic regularity of verse.
9. **Cover, T. M. & Thomas, J. A.** *Elements of Information Theory*, 2nd ed., Wiley (the proposal indicates 2008; the standard edition is 2006 — verify the edition actually cited) [S/T]. — Role: standard definitions and notation.
10. **Herrera, S., Silai, I.-M., Guillaume, B., Kahane, S. (2025).** "Extraction of Contrastive Rules from Syntactic Treebanks. A Case Study in Romance Languages". ACL Anthology 2025.quasy-1.5 (details of the QUASY venue to be completed) [P/T]. — Role: justification of the exclusions (PUNCT etc., §3.4).
11. **Anderson, P. W. (1972).** "More Is Different". *Science* 177(4047): 393–396. [S] — Role: conceptual/epistemological anchoring (Introduction/Discussion); **never operational**.
12. **Chomsky, N. (1956).** "Three Models for the Description of Language". *IRE Transactions on Information Theory* IT-2(3): 113–124. DOI: 10.1109/TIT.1956.1056813. [V, previous session] — Role: conceptual anchoring of the **misspecification limitation** (finite-memory Markov models are not models of the grammar; the instrument is a measuring device): Limitations section (+ possible mention in the Introduction). **Never** as operational justification of the method (that is [5] with the VLMC literature). Final placement: open writing decision, Phase 7.

## B. Sources added in the design phase (mandatory in the related work; D39)

13. **Galves, A., Galves, C., García, J. E., Garcia, N. L., Leonardi, F. (2012).** "Context tree selection and linguistic rhythm retrieval from written texts". *Annals of Applied Statistics* 6(1): 186–209. DOI: 10.1214/11-AOAS511; arXiv:0902.3619. [V 2026-07-06] — Role: **closest precedent** (selection of VLMC models for linguistic rhythm, European vs Brazilian Portuguese). Mandatory differentiation: rhythmic-accentual vs morphosyntactic alphabet; dialectal identity vs formal constraint; no inter-regime predictive transfer.
14. **Chen, S. L., Burns, P. J., Bolt, T. J., Chaudhuri, P., Dexter, J. P. (2024).** "Leveraging Part-of-Speech Tagging for Enhanced Stylometry of Latin Literature". *Proceedings of the 1st Workshop on Machine Learning for Ancient Languages (ML4AL 2024)*, pp. 251–259, ACL. [V 2026-07-06] URL: aclanthology.org/2024.ml4al-1.24/ — Role: it demonstrates that the prose/verse **classification** from POS features in Latin is solved and easy → repositioning of the novelty (erratum E8); their declared limit (short fixed-order POS n-grams) is exactly what the adaptive instrument overcomes; it also documents differences of annotation conventions between treebanks (relevant for D31).

## C. Methodological foundations required by the v2 architecture (Methods / related work strand ii)

15. **Rissanen, J. (1983).** "A universal data compression system". *IEEE Transactions on Information Theory* 29(5): 656–664. [V from snippet, 2026-07-06] — origin of the Context algorithm and of the context models.
16. **Bühlmann, P. & Wyner, A. J. (1999).** "Variable length Markov chains". *Annals of Statistics* 27: 480–513. [V from snippet, 2026-07-06] — VLMC statistical framework.
17. **Ron, D., Singer, Y., Tishby, N. (1996).** "The Power of Amnesia: Learning Probabilistic Automata with Variable Memory Length". *Machine Learning* 25 (issue/pages to be verified) [S/T]. — Probabilistic Suffix Trees in machine learning.
18. **Willems, F. M. J., Shtarkov, Y. M., Tjalkens, T. J. (1995).** "The Context-Tree Weighting Method: Basic Properties". *IEEE Transactions on Information Theory* 41(3): 653–664. [S] — CTW comparator (optional robustness, D32).
19. **Krichevsky, R. E. & Trofimov, V. K. (1981).** "The Performance of Universal Encoding". *IEEE Transactions on Information Theory* 27(2): 199–207 (details to be rechecked) [S/T]. — KT estimator (β = 1/2).
20. **Csiszár, I. & Talata, Z. (2006).** "Context tree estimation for not necessarily finite memory processes, via BIC and MDL". *IEEE Transactions on Information Theory* 52: 1007–1016. [V from snippet, 2026-07-06] — consistency of the MDL/BIC estimation of context trees.
21. **Galves, A. & Löcherbach, E. (2008).** "Stochastic chains with memory of variable length". In *Festschrift for Jorma Rissanen*, TICSP Series vol. 38, pp. 117–133; arXiv:0804.2050. [V from snippet, 2026-07-06] — VLMC survey.
22. **Holm, S. (1979).** "A simple sequentially rejective multiple test procedure". *Scandinavian Journal of Statistics* 6(2): 65–70 (details to be rechecked) [S/T]. — multiplicity correction (family {P1, P2}).

## D. Data resources (to be credited in the preprint)

23. **UD_Ancient_Greek-Perseus** (`grc_perseus`), UD v2.18 — 13,919 sentences; 202,989 tokens; UD conversion by G. G. A. Celano from AGLDT 2.1; licence CC BY-NC-SA 2.5. [V 2026-07-05] Page: universaldependencies.org/treebanks/grc_perseus/.
24. **UD_Latin-Perseus** (`la_perseus`), UD v2.18 — 2,273 sentences; 28,868 tokens / 29,223 syntactic words; 355 MWTs; same provenance and licence. [V 2026-07-05] Page: universaldependencies.org/treebanks/la_perseus/.
25. **AGLDT 2.1** (Ancient Greek and Latin Dependency Treebank, Perseus) — the source resource must be credited; candidate canonical reference: **Bamman & Crane 2011** (the existence of the reference is confirmed by the bibliography of [14]; exact title and venue to be verified) [T].

*End of the register. Every new source introduced during the project must be added here with status and role, before being cited elsewhere.*
