> **English translation; the Italian original governs** (V3-012).
> Original: `docs/TEST_INVENTORY.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `01684571b4c34e689a7a122a3e25b09b0cfdbdbbd5aab48a48d70c3cd33cc78b`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original; numbers use English notation, also inside formulas; link targets are reproduced unchanged and resolve as they did at `5f1ec06`. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# HEXIS 3.1 test inventory — V3-001

Active acceptance: marker `v31`; actual collection mandatory, asserts executed,
no skip/xfail/xpass. The comparison with the contract does not replace the CTW tests.

## Reconciliation of 18 September 2026 — M1–M5

The subsequent attestations keep the credit of their commits. The general V2 closure is verified on 22 September 2026 (final section); the residues listed here are closed.

| Requirement | Existing implementation and tests | Residue of the current review |
|---|---|---|
| M1 — CTW/numerics | `context_tree.py`, `diagnostics.py`; `test_v31_context_tree.py` T09–T16 | Integral comparison with §6/§12, rerun of the 25 synthetic cases and 9 stresses with distinct criteria |
| M2 — RNG/sample/shuffle | `sampling.py`; `test_v31_sampling.py` T05–T09/T17–T18 | Reconciliation with frozen vectors and reuses |
| M3 — scores/diagnostics/R1 | `scores.py`, `r1.py`; score/R1 tests T19–T23 | Reconciliation of formulas, two weights and nulls; no change to the expectations |
| M4 — persistence/semantics | `scientific_run.py`, `run_descriptive.py`, `run_report.py`; `test_v31_descriptive.py` | Actual lock, documents without targets, reconstruction of L/unseen, schemas/keys/denominators, per-model resources |
| M5 — evidence/checklist | `run_tree_validation.py`, `conftest.py` enforcement | Corpus/output mode, JUnit and v31 process linked to the manifest, stable context, versioned schema, preservation on resume, future check 42/84 distinct from 490/980 |

| ID | V0–V2 status | Coverage / residual obligation |
|---|---|---|
| T01 | V1 | Input/hash, sent_id, 18 prefixes/17 documents |
| T02 | V1 | Document/block and whole-corpus counts |
| T03 | V1 | Parsing, coordinates, identity, localized errors |
| T04 | V1 | Global mapping, inventories, C0/UPOS, inventory_only |
| T05 | V2 | Exclusion of held-out and `inventory_only` from training, in all six cells for seven folds |
| T06 | V2 | Exact q, no replacement, ≤1 fragment per contributor, empty and impossible budgets |
| T07 | V2 | Source order; sampler invariant to the order of the records and blind to the labels; reuse of ledger and permutation as declared |
| T08 | V2 | §12.2 vector and the seven deposited `block_key`s, separate purposes, repeatability, O/R coupling; no probe purpose active |
| T09 | V2 | Stream/reset and exact partition of the sample; terminal BOS and partition of the counts in T10–T11 |
| T10 | V2 | Independent enumeration of the admitted trees against evidence, root weight and prediction |
| T11 | V2 | Normalization, rare/unknown support, empty training, D=0, m100/105/11, strict inputs |
| T12 | V2 | Prequential/integrated pre-update identity; invariance to the order of the streams |
| T13 | V2 | Counts/evidences/weights/fingerprint unchanged by the evaluation |
| T14 | V2 | Extreme prior in log, two weights from δ, saturation distinct from forced leaves |
| T15 | V2 | 25 synthetic cases at the §12.1 thresholds on the canonical CTW; violation → non-zero exit |
| T16 | V2 | Historical m106 stress: execution, normalization, supports, recorded deficit |
| T17 | V2 | Length, multiset, mask and root counts preserved; slot distinct from provenance |
| T18 | V2 | Counterexamples of internal dependence and of heterogeneous pool at the level of the sample and in G/Q: non-null G_R with two fitted models |
| T19 | V2 | Four-term Q; archived counterexample of sign inversion reproduced on the canonical CTW |
| T20 | V2 | Aggregations/two weights |
| T21 | V2 | Coupled sensitivities |
| T22 | V2 | Masses/supports/L_resolved |
| T23 | V2 | R1 |
| T24 | CODE pre-V3, EXECUTION PENDING V5 | Census of the six inventory_only (V1); the report validator regenerates every ledger from the RNG contract, hence no held-out/inventory_only in training, and refuses every inventory_only scoring: code and tests in `0dc69b5`; execution on the campaign in V5 |
| T25 | PENDING V4 | Equality of the 490/980 model/pair keys |
| T26 | V2 | Atomicity/interruption, resume, corruption, duplicates and extra keys: corpus (V1) and scientific stage (V2) |
| T27 | CODE V2, EXECUTION PENDING V5 | Reconstruction of scores/diagnostics and five figures: code and tests on fixtures in `559dc40`, fixes of the pre-V3 review (samples, shuffles and C0 provenance regenerated; figures readable at the real cardinality) in `0dc69b5`; execution on the real data in V5 |
| T28 | V0–V1 | Pipeline without candidates/inference; acceptance without skips |
| T29 | PARTIAL V1 | Corpus identity/round-trip; samples and shuffles regenerated for every pair (`0dc69b5`); CE/reproduction of models PENDING V5 |
| T30 | PENDING V5 | Complete scientific report |

| Previous suite | Disposition and reason |
|---|---|
| test_conllu_reader.py, test_registry.py, test_g1_registry.py | KEPT: generic parsing/validations; active registry verified by test_v31_corpus/config |
| test_alphabet.py, test_g1_alphabet.py | KEPT historical with explicit v2.1 configuration; totality on unknown tags/IDs by frequency REPLACED in the active suite by T03/T04 |
| test_sequences.py, test_g1_sequences.py | KEPT generic/historical; SEP concatenation RETIRED in the active suite; streams and coordinates T03/T09 |
| test_run_audit.py | KEPT on the explicit historical audit; bilingual gate, provenance and v2.1 sidecar RETIRED in the active suite; defences reused and tested in T01/T26/T29 |
| test_determinism.py | KEPT hashing/writing and historical RNG (XOR/CRC32); scientific SHA-256 RNG REPLACED in the active suite by T08 |
| test_permutation.py, test_bootstrap_holm.py, test_blocks.py | KEPT working historical utilities, without imports in the descriptive pipeline |
| test_g0_enforcement.py, test_g1_enforcement.py, test_gate_inventory_anchor.py | KEPT historical checks; the same enforcement extended to v31 |
| test_docs_consistency.py | KEPT alignment of the G1 history and copies of the instructions |
| test_context_tree.py, test_tree_slices.py, test_scores.py, test_null_calibration.py | Historical scaffold, excluded from the v31 acceptance. Selector/slices/inference RETIRED; CTW, four scores and label-free core REPLACED in the active suite by T09–T23 |

The four deposited CTW fixtures are identified, not executed in V0–V1.
The 17 historical skips remain visible in the complete suite, never counted as acceptance.

## V0–V1 evidence concluded

- `test_v31_config.py`: deposit, field/type projection, duplicate YAML, retired parameters, historical isolation.
- `test_v31_corpus.py`: T01–T04, coordinates/numeric order/parts, masks/reset/targets, A/B diagnostics and semantic corruptions.
- `test_v31_persistence.py`: integrity of the three inputs, snapshot, identity, round-trip, collisions/concurrency, interruption, corruption and manifest schema.
- `test_v31_docs.py`: active authority, digests of the deposit and of the ten historical copies, absence of inferential/candidates imports in the pipeline.
- `test_v31_enforcement.py` and `test_gate_inventory_anchor.py`: nominal inventory compared with the actual collection, executed asserts, refusal of skip/xfail/empty tests and absent anchors.

Acceptance on the V1 code `7afdd3a`: **88 passed, zero skips**. Complete suite: **411 passed, 17 historical skips**.
The PENDING parts of the table remain so; V0–V1 does not promote T05–T30 in full to completed.

## V2 evidence — CTW core (T10–T16)

- `test_v31_context_tree.py`: independent enumeration oracle, BOS partition, normalization and
  core inputs, prequential identity, frozen model, numerics of the two weights, §12.1 battery.
- Battery executed by `hexis.pipeline.run_tree_validation`: 25 small synthetic cases all within the thresholds
  of the §12.1 table (**`iid` m=4 at the plan's threshold 0.02, not at the 0.03 of the historical script**) and
  nine m106 stress cases with recorded deficit, without a criterion of reaching the oracle.
- Complete suite after T10–T16: **456 passed, 17 historical skips**. At that point T05–T09 and T17–T30 remained PENDING.

## V2 evidence — sampling, RNG and shuffle (T05–T09, T17, T18)

- `test_v31_sampling.py`: the §5.3 deriver reimplemented independently in the test (only `hashlib`/`json`)
  and compared with the §12.2 vector — keys `held`/`fixture`, derived seed, `permutation(6)`, ledger
  `@1[0,5) @5[0,7) @4[0,2) @2[3,6)` and subseed `fragment` of `@2`; the **seven deposited `block_key`s**
  recomputed from their members.
- Exclusion verified on the real corpus for **six cells × seven folds**: never a document of the
  held-out block, never an `inventory_only` (not even if listed among the members), always six contributors with exact
  q. Plutarch contributing in C0 uses all its 8,884 tokens in 499 sentences without any fragment.
- Declared reuse (`hexis_v3.1_design.json.sampling`): `a_total1`/`D12`/`upos` reproduce the C0 ledger
  **byte for byte**; `q_half` and `oth` reuse only its order of the sentences and recompute stop and cut.
- The sampler reads `role` and the source coordinates: regime, group and `dependence_block` can
  be removed or falsified without changing the ledger, and the order of the records is irrelevant.
- T18 is closed at the level of the sample (identical multiset, different local dependencies; heterogeneous pool
  that remains non-i.i.d. after the shuffle). The comparison in G/Q on the same counterexamples remains at T19.
- Canonical order and support of the cut re-pinned against an independent transcription of §5.2 in the test
  (the identity of the sentence is not the key: `@10` precedes `@2` in lexicographic order) and against the
  complete coverage of the admitted offsets; the ledger withstands the parquet round-trip of the V1 artifact.
- Complete suite after T05–T09/T17–T18: **486 passed, 17 historical skips**.

## V2 evidence — scores and diagnostics (T18 residue, T19–T22)

- `test_v31_scores.py`: entirely synthetic fixtures (alphabets m=2..5, toy sentences, three blocks).
  **No fit on the Greek corpus**: the freeze of real fits until V3 applies also to the tests.
- T19: the archived counterexample of `diagnostics_validation.json` (Q≈0.7134571524694422, shortcut
  `CE_CTW_R−CE_CTW_O`≈−0.6650544707842875, root difference ≈1.3785116232537296) is **reproduced by the
  canonical CTW** within 1e-9 bits through `score_streams`/`aggregate`/`ce_gain_q`: the sign of the
  shortcut is opposite to that of Q. On the complete §7 path the four CEs per slot coincide with
  `CTW.evaluate` at the same tolerances, and the slots of the two arms are verified one-to-one.
- T18 (residue): heterogeneous pool of two dialects fitted on the two arms — G_R = 0.817 bits, Q = −0.216
  while G_O = 0.601: assuming G_R=0 would get even the sign wrong. Share of changed slots 18/44 read
  from `changed_count`/`total_count` of the shuffle, not recomputed.
- T20: losses→documents→blocks→groups on unequal lengths; the block CE is sum/targets
  (13/3), not the mean of the document means (5.5); the total is the sum of the two disjoint bands.
  The two weightings return the four CEs, G_O, G_R and Q, and `D_Q = D_G_O − D_G_R` is verified
  in `contrasts` for both; a block without scores interrupts the contrast.
- T21: ten seeds per cell, aggregation **per seed first** of the five statistics (SD with S−1,
  null at S=1); the coupled join refuses duplicates and different slot sets — the OTH case, where the
  population of targets changes, is not aligned by equal length.
- T22: R as direct sum (never `1-unseen_mass`), masses+unseen=1 within 1e-12, L_resolved null with
  reason `no_resolved_mass` with empty training and 0.0 on forced leaf D=0; mean as the sum of the valid values
  divided by the valid count; empty band with n=0, additive sums 0 and CE/G/Q null `empty_bucket`.
- The active public boundary is `pooled_score_core` (coupled slots, four losses,
  no label) plus `annotate_scores` (join with the registry without altering the scores).
  `score_streams` remains an alias of the same implementation. The signature tests in
  `test_scores.py` are adapted to the 3.1 vocabulary and included in the active acceptance;
  the inferential scaffolds of the same file remain historical.
- Complete suite after T18–T22: **498 passed, 17 historical skips**.

## V2 evidence — R1 (T23)

- `test_v31_r1.py`: its own fixtures (seven toy blocks, m=5), independent of the rest of V2 —
  R1 uses no CTW, sample or seeds (§8.3).
- Symmetry, zero diagonal, range [0,1] bits with the upper bound **reached exactly** on
  disjoint distributions (`0 log 0 = 0` without NaN), exact zero on coinciding distributions and sum
  of the per-symbol contributions equal to the JSD within 1e-15.
- `block_counts` counts **all** the retained tokens of the variant, including the first four non-eligible
  slots; `r_b=(n+0.5)/(N+0.5m)` compared element by element, with positive mass also for
  a symbol never observed in the block.
- 7×7 matrix and 21 pairs consistent with each other; centroids as the uniform mean of the blocks of the group and
  **a single JSD of the centroids**, numerically distinct from the mean of the pair JSDs
  (0.19507 against 0.19689 on the fixture).
- Complete suite after T23: **501 passed, 17 historical skips**.

## V2 evidence — scientific persistence, manifest and resume (T26)

- `test_v31_descriptive.py`: toy campaign (three documents, alphabet m=5, two blocks, two cells,
  one seed) published in a temporary V1 corpus and driven by the real CLIs. **No fit on the Greek
  corpus**: the freeze of real fits until V3 applies here too, and the file remains executable without `data/raw`.
- The toy contract **is not** the deposited analytical projection: for it both CLIs
  require `--fixture` and refuse it on the deposited configuration, and the report records
  `checks.scientific = False`. The synthetic campaign is not readable as a result.
- Manifest `hexis-scientific-manifest-1` distinct from `hexis-corpus-manifest-1`: `corpus_run` remains
  closed and only its format-agnostic utilities are imported from it without changes
  (`write_artifact`, `artifact_record`, `_read_json`, `check_destination`, `_code_identity`).
- Atomicity: writing to a temporary inside the destination, round-trip of every artifact, hard link
  of the new files only, `os.replace` of the manifest **last**, rollback on exception. An exception
  midway through writing leaves the bytes of the previous manifest intact; an orphan hard link surviving a
  kill makes the run invalid and blocks the resume until it is removed.
- Resume: a partition is reused only with identity, bytes/hash, schema, cardinality and keys
  coinciding. Refused: a changed configuration (`run_contract.configuration`), a changed corpus
  (`run_contract.alphabets`) and a changed code identity (`run_contract.code`); a resume without
  residual work is a no-op, not a second publication; the `report` stage closes the run.
- Corruption and keys: five faults on the artifacts (rewritten bytes, truncated parquet, absent file,
  cardinality falsified in the manifest, `run_id` falsified) and eight on the manifest (duplicated JSON
  key, non-finite value, unknown field, missing field, duplicated model key, extra model
  key, extra artifact on disk, unknown stage) are all detected, and none of them is reusable
  with `--resume`.
- Determinism: the same campaign in two destinations produces artifacts **byte for byte identical** and
  manifests equal in everything except `metadata` — timestamp, machine, paths and resources are external
  metadata, outside `run_id` and the seeds (§11.3).
- Report validator (§14.2): the six steps are executed in order and recorded in `checks.steps`;
  an incomplete campaign, an `inventory_only` scoring, evidence recorded under other code/lock
  and a second emission are refused before writing any table. The fixtures
  record V0/V1; the real report also requires V2/V3. Their deposit in the manifest
  remains part of the future V3 integration, it is not attested by the toy campaign.
- §13.2 retirements verified as behaviour: `run_confirmatory`, `run_null_calibration`,
  `run_reference`, `run_latin` and `run_sensitivity` declare the retirement in the docstring and exit with
  an explicit error; `model/lexicon.py` and `blocks.py` are not imported by the descriptive path.
- The five §11.6 figures remain outside V2: `viz/plots.py` is not touched and the report writes
  no figure (T27/T30 remain PENDING V5).
- Complete suite after T26: **543 passed, 17 historical skips**.

Acceptance on the V2 code `de8ea5d`: **220 passed, 340 deselected, zero skips**. Complete suite:
**543 passed, 17 historical skips**; `uv lock --check` unchanged on 23 packages. The intermediate
counts of the previous sections are snapshots taken at the end of each milestone, before
their review-fix commits; these two counts describe the first V2
closure, before the resumption documented below. The PENDING V4/V5 parts of the table remain so.

## V2 resumption — links and persistence, 2026-09-17

- T19/T20/T28: public APIs `pooled_score_core` and `annotate_scores` operational; scores and
  diagnostics byte-identical when the labels change, frozen fingerprint and a join that
  refuses duplicated/missing/null keys and overwriting of the scores.
- T26: atomic publication after each pair. Interruption before the second fit,
  resumption of the residual pairs and comparison with a new independent execution;
  same artifacts byte for byte. Selection of seed 0 only, refusal of the incomplete
  report and later completion without changing `run_id` or refitting the present pairs.
- T06/T26/T29: `sample_ledger__<sha256>.json` per distinct sample, referenced by the
  pairs and reused without overwrite; hash, cardinality and references verified also
  during resume. Synthetic regeneration of the original fingerprint from the reread ledger.
- T21/T26: comparison of the slot sets with the coordinates before discarding the
  vectors of the sensitivities; errors detected also at unchanged cardinality.
- T15/T16/T26: `run_tree_validation --config` validates the deposited projection;
  atomic output, refusal of the collision with another writer and protection of the
  raw data also through symlinks and with `--force`.
- The nominal collection in `test_v31_enforcement.py` includes all these new checks.
  No expected scientific test, threshold, seed, raw datum or contractual byte modified.
  Only the expectations of the signatures of the v2.1 protocol are replaced, as recorded
  in the V3-001 execution note; the label-free boundary remains mandatory.

Acceptance on the bytes of the resumption committed in `d38b5a7`:
**240 passed, 338 deselected, zero skips**.
Complete suite: **561 passed, 17 historical skips**. Lock unchanged, 23 packages.
The 20 active cases added comprise 18 new cases and the two pre-existing
signature tests; the integral review and V3–V5 remain outside this attestation.

## Reconciliation 2A — 2026-09-18

T11/T17/T22: support histograms per depth with BOS; counter of unobserved encounters independent of the underflow; unique slots across streams, bijective provenance and validation of all the symbols of the core. T15/T16: complete battery by exact set of the cases, counts, finite values, normalization, supports, deficits and oracle regenerated from the fixture. The 25 synthetic cases respect the frozen thresholds; the nine stresses need not reach the oracle. Acceptance: **262 passed, 338 deselected**, no skip/xfail. No generator, seed, threshold or contract modified.

## Reconciliation 2B — 2026-09-18

M4/T22/T26/T27/T29: `test_v31_completion.py` and `test_v31_report_semantics.py` cover the present lock, empty rows, per-model resources external to the identity, artifact arms/families, key types and semantic corruptions in report/resume also after recomputation of the hashes. The C0 sums of the four losses, L_resolved and unseen are reconstructed; exact counts/keys, CE within 1e-9 bits/target and diagnostics within 1e-12 per position. Schemas, duplicates, nulls, masses, supports and denominators verified also in the sensitivities. R1 keeps empirical and smoothed frequencies. Acceptance: **302 passed, 338 deselected**, zero skip/xfail. The real modelling checks, prefixed regeneration and figures remain for V3–V5; this coverage is synthetic.

## 2C closure, integral review and completion of the report — 2026-09-22

- M5/T26/T29 (`482cef0`) — `test_v31_validation_run.py`, now in the mandatory inventory: acceptance compared with JUnit and the actual collection; vacuity, skips and failures refused; V2 evidence kept on resume; missing evidence, hand-written PASS, altered context, JUnit or process block the fits; technical set 42/84 only on fixtures; real fits only with clean tracked producers; V3 record recomputed, never trusted.
- Report contract (`f3f8a65`): `test_diagnostics_carry_the_report_contract_names` reads `report_contract_v3.1.json` and checks its aggregated fields, per-arm diagnostics (`…_by_reason_*`, `…_by_length_*` as families), shuffle counts and columns of `model_diagnostics.csv`, resources included.
- M4/T11 (`5dc7d1b`): `training` and `fragments` recomputed from the persisted ledger, with the `training`/`fragments` faults in `test_partition_semantic_corruption_is_rejected`; empty training → zero observed nodes (§9.1).
- T20/T21/T27/T29 (`0a6f644`): `test_report_summarizes_every_level_and_pairs_sensitivities_per_block_and_seed`, `test_empty_document_summaries_stay_null_with_their_reason`, `test_seed_zero_regeneration_is_compared_and_recorded_by_the_report`, `test_a_scientific_report_requires_the_seed_zero_regeneration`.
- M1–M4: independent checks of the review in the [handoff](HANDOFF.md).
- The previous sections describe the state at their commits: `hexis-scientific-manifest-1` is replaced by `-2`, and `changed_count`/`total_count`, `observed_mass_*` and the other previous names by those of the contract.
- Before V3: the five §11.6 figures (T27), because the code identity covers all of `src/hexis`. T25 remains V4; T24/T27/T29/T30 remain V5 as execution and verification.

Acceptance on the code `0a6f644`: **328 passed, 338 deselected**, zero skip/xfail. Complete suite: **649 passed, 17 historical skips**.

## Five §11.6 figures — 2026-09-22

T27 (`559dc40`), `test_v31_figures.py` in the mandatory inventory: the five figures with the names of `report_contract_v3.1.json`, deterministic SVGs with the `run_id` and without date, plotted values equal to those of the tables (profiles, D_Q, R1 matrix, PART shares), structured columns of `model_diagnostics.csv` in canonical JSON, no import of model, sampler, pipeline, `pyplot`, `stats` or `candidates` in `viz/plots.py`. The identity between two destinations also covers the figures. This satisfies the «before V3» obligation of the previous section; the execution on the real data remains V5.

Acceptance on the code `559dc40`: **332 passed, 338 deselected**, zero skip/xfail. Complete suite: **653 passed, 17 historical skips**.

## Integral pre-V3 review — 2026-09-22

Fixes in `0dc69b5`, each with a red test before the code (detail and decisions D1–D4 in the [handoff](HANDOFF.md)):

- T05/T08/T24 on the campaign: `validate_partitions` regenerates with `sampling.pair_streams` the ledger of every pair, the shuffle counts and, in C0, the shuffled provenance. `test_the_persisted_ledger_is_the_contract_sample_even_after_rehashing` (held-out sentence, `inventory_only` sentence, moved cut, all re-hashed consistently) and `test_shuffle_counts_and_c0_provenance_are_the_contract_regeneration`.
- Seven validator guards that the mutation showed never exercised, now pinned with `match=`: `test_each_c0_guard_names_its_own_corruption`, `test_sensitivity_partitions_enforce_diagnostic_denominators_and_bounds`, `test_contrasts_refuse_a_q_that_is_not_the_gain_difference`.
- T27, figures: C0 masses up to its depth, labels «author, work (n=…)» and order by group, names of the symbols in the R1 tables, declared order of the cells; `test_every_figure_keeps_its_text_inside_the_canvas` uses the seventeen labels of the deposited registry and three R1 representations.
- Exhaustive inventory: `REQUIRED` comprises all the 181 defined v31 tests (8 were outside) and `test_v31_inventory_lists_every_collected_active_test` enforces it.
- Mutations (copy in scratchpad): 35 guards out of 40 detected; the 5 survivors are dominated by a stronger check (roles per partition and at step 5 by the comparison of the document/band keys; overwriting in `annotate_scores` by the refusal of pandas; comparison on resume by the name-digest; denominator of the shuffle by its regeneration).

Acceptance on the code `0dc69b5`: **351 passed, 338 deselected**, zero skip/xfail. Complete suite: **672 passed, 17 historical skips**. The PENDING V4/V5 parts of the table remain so.
