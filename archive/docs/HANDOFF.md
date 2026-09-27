> **English translation; the Italian original governs** (V3-012).
> Original: `docs/HANDOFF.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `6cf7a46d7d0f779aa9d07709e20d44b1db8e2208dbc27f17275ca232cf1305a0`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original; numbers use English notation; commands and outputs are reproduced unchanged, and the comments inside the command blocks are translated; link targets are reproduced unchanged and resolve as they did at `5f1ec06`. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# Handoff HEXIS 3.1 — V3-001 — V2 reconciliation

## Integral pre-V3 review — 22 September 2026

**V0–V2 completed; code and tests final for V3 after this review; V3–V5 not attested; no real fit; no push.** The integral review requested by the user (read-only, at `a123278`) reproduced the previous attestation (332/653+17/lock 23), verified the 63 digests of the deposit, the v2.1 history byte for byte against `852644b` and the two V1 runs, and found defects then fixed test-first in the code commit `0dc69b5`. The documentary commit that contains this section does not cite itself.

**Owner's decisions (22/09/2026).** D1: no public push until a publication act decides on the derivatives; the deposit contains `HEXIS_v3_allegati/verifiche_CTW_precedenti.zip` → `ctw_validation/pilot_positions_example.npz`, 46,634 per-position losses of the Homeric targets of the historical pilot (65 distinct values of `root_loss`, a function of the symbol in each position), that is a per-position derivative that §17.3 leaves local. D2: the validator regenerates ledgers, shuffle counts and C0 provenance. D3: the deviation of the CLI from §14.1 is recorded in the V3-001 note of the [Decision Log](02_DECISION_LOG.md). D4: figures corrected in their defects and readability.

**Fixes (`0dc69b5`).**
- T05/T08/T24 on the campaign: `run_report.validate_partitions` regenerates with `sampling.pair_streams` (shared with `run_pair`, output identical byte for byte) the ledger of every pair, the shuffle counts and in C0 the shuffled provenance; before, a tampered and re-hashed ledger with a held-out or `inventory_only` sentence passed. Cost measured on the real corpus 0.2–0.3 s per pair.
- Figures: fig. 5 drew the C0 masses at zero for ℓ = 9…12 (empty D12 columns summed); fig. 2 labelled the documents with the raw `doc_id` and now shows «author, work (n=…)» (dominance of the Iliad, §3.3) with blocks in group order; fig. 1 had a truncated title; fig. 4 now names the symbols (column `symbol` in the R1 tables) and had a truncated title with three representations; fig. 3 follows the order of the cells of the contract. Previews inspected: fig. 1 and 4 on the real V1 data, fig. 2, 3 and 5 at the real cardinality with dummy values, without fits.
- Tests: v31 inventory exhaustive and enforced (8 active tests were outside it); the seven validator guards never exercised pinned with `match=`. Mutations on a copy: 35 of 40 detected, the 5 survivors dominated by stronger checks ([inventory](TEST_INVENTORY.md)).
- `ponytail` comment of `run_descriptive` rewritten: the revalidation at every publication costs about 8 s per pair for the corpus plus a quadratic growth, estimated at about 2 h over 490 pairs; making it faster after V3 is a new identity and redoes V3.

**Freeze perimeter.** `_code_identity()` covers all of `src/hexis`; the V2 evidence (`validation_run.context`) also binds `tests/*.py`, `conftest.py`, `pyproject.toml`, the configuration file, `uv.lock` and the manifest of the corpus used. A change to one of these after the publication of the validation prevents the resume and requires a new directory with V2 and V3 redone. The documents remain modifiable.

**Operational sequence planned for V3–V5, not executed.** Clean tracked tree (untracked `scripts/` is admitted), corpus `results/hexis31/v1`, new destinations under `results/hexis31/`:

```bash
uv sync --frozen
uv run python -m hexis.pipeline.run_tree_validation --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<run>
uv run python -m hexis.pipeline.run_descriptive --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<run> --seed 0
# §12.2: same pair of commands in a distinct directory, same code
uv run python -m hexis.pipeline.run_tree_validation --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<regen>
uv run python -m hexis.pipeline.run_descriptive --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<regen> --seed 0
# V4, after the review of V3
uv run python -m hexis.pipeline.run_descriptive --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<run> --resume
# V5
uv run python -m hexis.pipeline.run_report --config config/default.yaml --corpus-dir results/hexis31/v1 --output-dir results/hexis31/<run> --regenerated-dir results/hexis31/<regen>
```

**Deposit.** The V0 commit `e98fb8e` had deposited 64 files, among them `hexis-verifica/.DS_Store` (Finder metadata, sha256 `18cc90e9ff3e6473b1790a06f5bbf5afb3be60f5359284118c94b4f8383df96b`, absent from `hexis-verifica/SHA256SUMS.json` and still present in the original on the Desktop). The V1 commit `7afdd3a` removed it together with its row in `V3-001-deposit.json`, without documenting it. The remaining 63 digests are unchanged and match the tracked files; `.DS_Store` is now in `.gitignore`.

Commands on the bytes of `0dc69b5`, final lines verbatim, all exit 0:

```text
uv run --frozen pytest -m v31 -q -p no:cacheprovider
351 passed, 338 deselected in 180.99s (0:03:00)

uv run --frozen pytest -q -p no:cacheprovider
672 passed, 17 skipped in 200.10s (0:03:20)

uv lock --check
Resolved 23 packages in 12ms
```

Local commits only. Stop for review before V3.

## §11.6 figures — 22 September 2026

**V0–V2 completed; the code needed before V3 is complete; V3–V5 not attested; no real fit.** The constraint recorded in the V2 closure below is satisfied in `559dc40`: `viz/plots.py` replaces the v2.1 stub with the five figures of the contract (`corpus_annotation`, `block_document_profiles`, `sensitivities_two_weights`, `R1`, `supports_mixture_masses`), drawn only from the verified tables and published by `run_report` as deterministic SVGs, with text in English. No figure computes quantities of its own beyond the single aggregation of `scores`/`diagnostics`; no inferential interval, only computational min–max across seeds. The review also corrected `model_diagnostics.csv`, which wrote the support histogram as a Python repr: the structured columns are now canonical JSON. Signatures approved by the owner; checks on fixtures, real execution in V5.

Commands on the bytes of `559dc40`, final lines verbatim, all exit 0:

```text
uv run --frozen pytest -m v31 -q -p no:cacheprovider
332 passed, 338 deselected in 162.20s (0:02:42)

uv run --frozen pytest -q -p no:cacheprovider
653 passed, 17 skipped in 168.70s (0:02:48)

uv lock --check
Resolved 23 packages in 3ms
```

Local commits only, no push. Stop for review before V3.

## V2 closure — 22 September 2026

**V0–V2 completed; V3–V5 not attested; no new real fit.** This section closes the residues M1–M5 of the correction of 18 September, which remains as history, after the integral review requested before V3. Closure code `0a6f644`, after `482cef0`, `f3f8a65` and `5dc7d1b`; the documentary commit that contains this section does not cite itself. Local commits only, no push.

**Resumption after the interruption of sub-stage 2C: no damage.** Three Greek CoNLL-U files with the hashes of the contract, clone at `37837c7`; plan, 3.1 attachments, 3.0.1 ZIP and `hexis-verifica` identical byte for byte to the Desktop; `uv.lock` `33db43b0…` and `uv lock --check` unchanged; `scripts/reacquire_raw_data.sh` at the recorded digest, untracked and preserved; V1 manifests `154433c7…`/`de08d13d…` valid, nine artifacts identical between the two directories; under `results/hexis31/` only the three V1 directories. The uncommitted 2C work was consistent (318 v31 pass) and was kept.

**2C/M5 — `482cef0`.** Stage `validation` in the manifest `hexis-scientific-manifest-2`: §12.1 battery, `pytest -m v31` process and JUnit compared as sets with the actual collection. No real fit without it; complete campaign only after the V3 record of seed 0 (42/84, distinct from 490/980). Fixed test-first: a hand-written V3 record with correct code/lock was accepted — now every recorded V3 is recomputed from the published run; `test_v31_validation_run.py` was missing from the mandatory inventory. Proved on fixtures; on the real suite the mechanism collected 321 tests and 321 matching JUnit cases, without publishing any run. The V2 evidence on the deposited configuration is produced at the opening of V3, with the code frozen.

**Integral review, with independent checks.**
- CTW against an enumeration of the trees written from the §6 formulas (26 trees): identical log-evidence, prediction within 1e-15.
- §12.1 battery rerun: 25/25 within threshold; lag 2 m106 stress CE 5.09–5.13 against oracle 1.13109; generator identical (AST) to the fixture `e6a55b08…`.
- §12.2 vector recomputed with `hashlib`/`numpy` only; six cells identical to §10; on the real corpus, without fits, seven folds × two seeds: ledger C0 = a_total1 = D12 = upos, q_half prefix of the C0 order, budget 53,304/26,652.
- §7 counterexample reproduced (Q 0.71346; shortcut −0.66505). No test weakened since `852644b`; the only replacement of expectations (v2.1 signatures) is recorded in V3-001.

**Defects found by the review and fixed test-first, on the owner's decision.**
- `f3f8a65`: eight persisted fields with names different from `report_contract_v3.1.json`, now identical and bound by a test that reads the deposited contract; per-model resources in `model_diagnostics.csv` (§11.5), with the identity between destinations exempting exactly those three measured columns.
- `5dc7d1b`: `training` and `fragments` of the pairs were not verified against the persisted ledger, and `training` feeds the training shares of the report; now they are recomputed from the ledger. With empty training the unobserved root no longer counts as a node (§9.1, a case not reachable in the real cells).
- `0a6f644`: the report code is part of the run identity, so everything the report must emit exists before V3 — summaries across seeds for groups, blocks and documents (§8.2); paired differences of the sensitivities per block/seed and per group/seed (§10); group shares of the training per fold (§5.1); table of the fragments (§11.5); `compare_regeneration` for the regeneration of seed 0 (§12.2), required by the scientific report (§14.2 step 6). The tool exists and has not been run on real data.

**Constraint before V3.** `_code_identity()` covers all the 39 files of `src/hexis/`, and the report refuses a run with another identity. The five figures of §11.6 (T27) are not implemented: `viz/plots.py` is still the v2.1 stub. They must be implemented and verified on fixtures before the V3 freeze, after approval of the signatures; otherwise the V5 work would change the `run_id` of V3/V4.

Commands on the bytes of the closure commit (code identical to `0a6f644`; only documents and documentary expectations of the tests change), final lines verbatim, all exit 0:

```text
uv run --frozen pytest -m v31 -q -p no:cacheprovider
328 passed, 338 deselected in 148.75s (0:02:28)

uv run --frozen pytest -q -p no:cacheprovider
649 passed, 17 skipped in 153.77s (0:02:33)

uv lock --check
Resolved 23 packages in 3ms
```

Stop for review before V3.

## Correction of 18 September 2026

**V0–V1 completed; V2 largely implemented, closure to be reconciled and verified; V3–V5 not attested.** The general statement of V2 completion in the following attestations is corrected: the counts and the properties demonstrated remain evidence of the commits cited, but they do not cover the residues M4/M5 nor the integral review now requested. The previous dated sections are kept as a historical account, including the deferrals to the integration that this tranche must complete. No new real fit nor rewriting of the proposal.

The new execution starts from `8b4d50432724442465d4d3003a2d37717395126a`, branch `codex/hexis31-v0-v1`; initial state `?? scripts/`, no tracked change. Work proceeds on the requested branch in the existing checkout. Local script and historical results remain preserved. The [review register](V2_RECONCILIATION.md) tracks sub-stages, digests and checks; the [inventory](TEST_INVENTORY.md) distinguishes implementation, proofs and gaps.

## Previous attestations (state referred to the commits cited)

**V0–V2 completed; V3–V5 not attested; no new real fit.** V0–V1 state verified on 16 September 2026, V2 state on 17 September 2026. Local branch: `codex/hexis31-v0-v1`.

## Revisions and authority

- Verified base: `852644b6917790877c7b2ca5df2e76b17829d87c`.
- V0, deposit and normative migration: `e98fb8edde91e821c415e26f33b7bdeb549b50ba`.
- V1, corpus and persistence: `7afdd3a4f87341110b0f15a77179febe9075ee9b`.
- V0+V1, documentary attestation: `b607cef434ffa8698cb2e4ca0387d2b759a18862`.
- V2, core and protocol, four milestones closed in sequence: `105c0aae26f4eb9b54267e02ee45f5449e565ac6`, `3119517da223940cc51eabaef096508c33c6ec03`, `e9c8c96e4573fb9585f4250ce38f47d5cc3a2998`, `de8ea5d576c415aa6bc082186b8ce649271a664b`.
- V2 resumption and completion of the links/persistence: `d38b5a7`.
- The final update of this handoff is documentary and cites the previous implementation commit, without self-references.

Authority: [active specification](01_MASTER_SPEC.md), [V3-001](02_DECISION_LOG.md) and the byte-identified plan/JSON in `contracts/hexis-3.1/`. The [external record of the deposit](V3-001-deposit.json) keeps the digests; no normative byte or expectation was updated to make the checks pass. Verified 8 digests of the delivery, 14 of the verdict/evidence, 33 files of the historical package, 103 of the inner archive and the four CTW fixtures. The fixtures were not executed as historical programs.

The ten v2.1 copies are compared with the originals through the [SHA-256 inventory](history/v2.1/SHA256SUMS.json). D01–D54, the proposed D55, the G1 technical ratifications, the proposal and the previous materials keep their historical status. The sources/limitations of the earlier authorizations remain in V3-001 and in §2 of the plan; no retroactive G2.

## Commands and results actually executed (V0–V1)

```bash
uv lock --check
uv run pytest -q
uv run pytest -q -m v31
.venv/bin/python -m hexis.pipeline.run_audit --config config/default.yaml --data-root data/raw/UD_Ancient_Greek-Perseus --output-dir results/hexis31/v1
.venv/bin/python -m hexis.pipeline.run_encode --config config/default.yaml --data-root data/raw/UD_Ancient_Greek-Perseus --output-dir results/hexis31/v1
.venv/bin/python -m hexis.pipeline.run_encode --config config/default.yaml --data-root data/raw/UD_Ancient_Greek-Perseus --output-dir results/hexis31/v1-reproduction
```

All exit 0. The `.venv` interpreter is the Python 3.12 environment managed and synchronized by uv. `uv lock --check`: 23 packages resolved, lock unchanged. Complete suite: **411 passed, 17 skipped**, all historical scaffolds; active acceptance: **88 passed, 340 deselected, zero skips**. New tests written and run red before their implementations. An independent review of configuration, corpus, persistence and history found no blocking problems.

The checks include localized parsing errors, missing/extra/altered inputs and inputs changed during the run, reordered records and numeric coordinates, Athenaeus XII/XIII, synthetic empty sentences, public unknown UPOS, global mapping and subtypes, C0/UPOS masks, exclusive inventories, A/B denominators, executed asserts and nominal collection, round-trip, corruptions at unchanged cardinality, collisions and interrupted writes. Atomicity through temporaries in the destination and exclusive publication with hard links; manifest replaced atomically last. This technical choice prevents overwrites even in a collision between check and publication.

## Real executions and identity (V1)

Common identity: `a04db5ca9bdfec4e9444fc01745c7210862eaebe5654bb8046b545bfbe154d42`.

- [Main manifest](../results/hexis31/v1/manifest.json), SHA-256 `154433c772f41e444f86b8787e0ee0003c546d9fb398b6ee0f634ce193f3421f`.
- [Reproduction manifest](../results/hexis31/v1-reproduction/manifest.json), SHA-256 `de08d13de608b33b4618b26b95359226179ad1c62c681e1104a151cca7611ef8`.
- Lock: `33db43b00bcb21ab12aedf6dcc4257764770bff0115dc0d1dfab6e5ea89876bf`.

Both record the V1 commit, the distinct V0 commit and `tracked_dirty=false` at the time of execution. `completed_stages=[audit, encode]`, `corpus_complete=true`, `scientific_complete=false`. The manifests differ in the external metadata (directory/timestamp), excluded from the identity. **All nine artifacts, including keys, contents, schemas and cardinality, are identical byte for byte in the two directories.** `validate_run` reread and verified both executions; additional comparison of the bytes of each file passed.

| Artifact | Cardinality (rows or JSON members) |
|---|---:|
| `alphabets.json` | 3 |
| `audit_A.csv` | 29 |
| `audit_contingency.csv` | 2075 |
| `audit_summary.csv` | 84 |
| `coordinates.parquet` | 530720 |
| `documents.csv` | 51 |
| `exclusions.parquet` | 78247 |
| `sequences.parquet` | 41757 |
| `source_audit.json` | 9 |

Exact recount: **202,989 source tokens, 13,919 sentences, 18 prefixes, 17 documents**, 11 primary in seven blocks and six `inventory_only`. Three alphabets **100/105/11**, with **9/10/0** types exclusive to the inventory-only documents. **51 documents/variant, 41,757 sentences/variant, 530,720 retained coordinates**. Checks A and B: zero reports; they remain diagnostic. All the documentary, block and population expectations coincide, not only the totals.

The active provenance is in [data/provenance_v31.json](../data/provenance_v31.json), outside raw. Three Greek inputs and source commit `37837c7a3c592c9563f8c51cc63344b87247f8a5` verified. Greek/Latin raw data, historical provenance, previous results and local script preserved. The real derivatives are local/ignored by Git; no publication of the data. `v1-development` keeps an earlier technical trial under a different identity; it is not the delivered run.

## Commands and results actually executed (V2)

```bash
uv lock --check
uv run pytest -q
uv run pytest -m v31 -q
```

Rerun on the code `de8ea5d`, all exit 0. `uv lock --check`: 23 packages resolved, lock unchanged. Complete suite: **543 passed, 17 skipped**, the same historical scaffolds of V0–V1. Active acceptance: **220 passed, 340 deselected, zero skips**. The §14 criterion for V2 — «Exact/synthetic tests and relevant checks T01–T23/T26 passed, without skips» — is satisfied: the [inventory](TEST_INVENTORY.md) brings T05–T23 and T26 to V2, and T01–T04 remain covered by V1.

The four milestones were written test-first and reviewed one by one: CTW core, numerics of the two weights and frozen §12.1 battery (T10–T16); sampling, RNG identity against the §12.2 vector and coupled order control (T05–T09, T17, T18); four losses, aggregations in the two weightings, diagnostics and R1 (T19–T23); scientific persistence, manifest `hexis-scientific-manifest-1`, CLI, resume and the §13.2 retirements (T26). The evidence per ID is in the inventory, not duplicated here.

## Resumption after interruption — 2026-09-17

The resumption starts from `feb23af`: the milestones and the first V2 attestation were already
committed, with only `scripts/reacquire_raw_data.sh` untracked. The initial
check reproduced **220 passed, 340 deselected**, without skips. The existing
work was kept; the links remaining in the
V2 path were completed, with red tests observed before the changes:

- Public APIs `pooled_score_core` and `annotate_scores` operational, without a new
  scoring formula; the labels are added to the fixed scores.
- `--seed 0` selection without altering configuration or identity, publication
  after each pair and actual resumption after an interruption between pairs.
- Complete ledgers `sample_ledger__<sha256>.json`, shared by the pairs that
  reuse the sample, with references/hashes/cardinality verified on reading.
- Check of the slot sets also in the sensitivities before discarding the
  vectors; configuration of the synthetic battery validated and atomic output,
  protected from collisions and raw destinations also via symlink.
- The V0/V1 records alone no longer allow the emission of a real report;
  the V2/V3 evidence will be linked in the integration, not simulated here.

Commands executed on the bytes then committed in `d38b5a7` and final lines verbatim,
all exit 0:

```text
uv run pytest -q
561 passed, 17 skipped in 87.22s (0:01:27)

uv run pytest -m v31 -q
240 passed, 338 deselected in 79.63s (0:01:19)

uv lock --check
Resolved 23 packages in 4ms
```

After the final alignment of the texts, the 12 documentary tests passed.
An earlier invocation limited to documentation and inventory had obtained
exit 1 because the collection check requires the whole acceptance: the
partial selection did not contain the other mandatory tests. No check
was weakened; the two complete suites above verified the collection.

The 20 additional active tests comprise 18 new cases and the two signature checks
already existing, now also included in v31; the 17 skips all remain historical.
The independent comparisons of the fixtures verify identity and artifacts byte for
byte both between two destinations and between a resumed execution and a new one;
the original fingerprint is also regenerated from the ledger reread from disk.
The complete battery keeps the 25 synthetic cases and the nine m106 stresses at the
deposited thresholds. No numerical expectation was regenerated.

Plan, four JSON files and `design_lock.json`: **six byte-for-byte comparisons with the
Desktop passed**. `uv.lock` remains
`33db43b00bcb21ab12aedf6dcc4257764770bff0115dc0d1dfab6e5ea89876bf`.
Under `results/hexis31` only the manifests `v1`, `v1-reproduction` and
`v1-development` remain. No new real fit, no publication, local script
and historical materials preserved. Stop for the next review before V3.

## V2 produces no real executions

V2 has no section of real executions and identity, and not by omission: by design it runs no campaigns and publishes no scientific artifacts. `results/hexis31/` still contains only the V1 directories already attested; no real scientific manifest exists. Plan §14 sets the boundary: «The new real fits start only in the integrated trial, after V0–V2 in the new authorized path». The completion criterion of V2 is therefore test coverage, not a run.

CTW, four scores, diagnostics, R1 and scientific persistence are verified on entirely synthetic or analytical fixtures: toy alphabets m=2…5, toy sentences, three and seven blocks, three documents, two cells and one or two seeds. For these toy configurations the two CLIs require `--fixture` and the report records `checks.scientific = False`. The deposited analytical projection is already accepted without `--fixture`; the `--fixture` option refuses it. The previous sentence according to which the CLIs worked only on fixtures was inexact: this resumption corrects the documentation, without running real fits.

A single contact with the real corpus remains in V2, and it is of sampling, not of modelling: `tests/test_v31_sampling.py` rebuilds the V1 corpus from the three Greek inputs to verify, on six cells × seven folds, that no held-out document and no `inventory_only` enters the training and that the ledger is the declared one. No model is fitted there, exactly as in the V1 corpus tests.

## Residual obligations (state at 17 September, superseded by the closure of 22 September)

The [inventory T01–T30](TEST_INVENTORY.md) distinguishes the V0–V2 coverage from the parts still PENDING. V2 is concluded: CTW, sampling/RNG/shuffle, core behaviourally independent of the labels, four losses, diagnostics, R1 and resume exist and are covered, with the exact fixtures and the 25 synthetic cases at the frozen thresholds. Still PENDING are the modelling part of T24 and T29, T25 in V4, T27 and T30 in V5.

V3 remains the next tranche and is not opened by this handoff: one seed (0) for all six cells, resource measurements, freeze of code and environment, for **42 pairs / 84 technical models**, finite/consistent, zero probes and final schema verified. `run_descriptive --seed 0` selects this subset without modifying the analytical configuration or the `run_id`; the following execution without `--seed`, with `--resume`, completes the planned seeds.

At the opening of V3 it remains to link to the manifest the proof of the V2 acceptance and that of the V3 integration under the actual code/lock. The executor today records from the verified bytes only V0/V1: the real report now refuses these two records as sufficient evidence, while the report of the fixtures remains available and non-scientific. The V2 suite does not attest this future integration. V4 remains the campaign **490 pairs / 980 model identities**; V5 remains report, five figures, two weightings, resume and prefixed regeneration.

The instructions `AGENTS.md`/`CLAUDE.md`/`04_AI_HANDOFF_PROMPT.md`, the active specification and the pytest marker are realigned to the V0–V2 state. Implemented code, synthetic acceptance and scientific results remain distinct: no instruction opens V3 automatically. The integral review is deferred as requested by the user; this resumption completes links and checks of the V2 plan, it does not attest a new integral review.

Rewriting of the proposal and publication are separate activities. The old [v2.1 handoff](history/v2.1/HANDOFF.md) is kept in full.
