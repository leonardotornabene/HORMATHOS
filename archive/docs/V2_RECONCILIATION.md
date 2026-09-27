> **English translation; the Italian original governs** (V3-012).
> Original: `docs/V2_RECONCILIATION.md` at commit `5f1ec06` (tag `archive/pre-realign`), kept at this path until V3-012; SHA-256 `028f8f4832c4e9cdc26a6af1805c17a186b55f2e5ee5b86d368b9ec6177d784e`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original; numbers use English notation; commands, outputs and code blocks are reproduced unchanged; link targets are reproduced unchanged and resolve as they did at `5f1ec06`. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# HEXIS 3.1 — V2 reconciliation register

User plan: realignment → 2A M1–M3 → 2B persistence → 2C evidence → separate review → closure; no real V3 fit, push or merge. Base `8b4d50432724442465d4d3003a2d37717395126a`, branch `codex/hexis31-v0-v1`, requested checkout already active, only `?? scripts/` initially. Authority: V3-001 and the deposited plan/JSON; expectations immutable.

Initial SHA-256 digests:

```json
{
  "docs/V3-001-deposit.json": "e0d8951f60e6eebaa31e957db7c8733fe30b3b09ce9f3db8cbece397c3d2694c",
  "uv.lock": "33db43b00bcb21ab12aedf6dcc4257764770bff0115dc0d1dfab6e5ea89876bf",
  "scripts/reacquire_raw_data.sh": "4524ac4162250520cf73283aa4b66bd4a22a6164ab8b4cd512741425f116b2bb"
}
```

| Sub-stage | Status | Evidence |
|---|---|---|
| 1 — realignment | COMPLETED — a535484 | 12 documentary tests passed; historical attestations kept |
| 2A — M1–M3 | COMPLETED | 262 v31 pass; 25 synthetic + 9 stress; separate review of the fixes passed |
| 2B — M4 | COMPLETED | 302 v31 pass; 86 targeted tests pass |
| 2C — M5 | COMPLETED — 482cef0 | V3 recomputed; complete inventory; mechanism proved on fixtures and on the real suite |
| 3 — integral review | COMPLETED — f3f8a65, 5dc7d1b, 0a6f644 | Independent checks; defects fixed test-first |
| 4 — closure | COMPLETED | V2 closed; §11.6 figures implemented (559dc40); stop before V3 |

The change to the documentary tests replaces the expectation of an unjustified general statement with the correction requested by the user; it does not weaken scientific properties.

## 2A — checks and demonstrated divergences

Base reproduced: `uv run pytest -m v31 -q` → `240 passed, 338 deselected in 87.27s (0:01:27)`; documentation after the correction → `12 passed in 0.12s`.

The M1–M3 comparison found missing support histograms (§9.1), encounters with unobserved branches lost when the mass underflows, duplicated slots/non-bijective provenance and invalid symbols not refused by the score path. Twelve regressions first red, then green. Generators, RNG, CTW/Q/R1 formulas and frozen expectations remain unchanged.

The battery returned success with missing/duplicated rows, non-finite or unnormalized stress, corrupted counts/supports/deficits and a PASS inconsistent with the losses: ten failures observed before the fix. The separate review also required the comparison of the recorded oracle with the frozen fixture. The nine stresses keep a criterion of numerical validity, without requiring them to reach the oracle.

Targeted protocol check: `uv run pytest -q tests/test_v31_scores.py tests/test_v31_r1.py tests/test_v31_sampling.py` → `58 passed in 16.50s`. A first check of the new validator also refused valid NumPy log-evidences; the explicit float64→native float serialization in the record corrects the type without changing the value.

2A closure: `uv run pytest -m v31 -q` → `262 passed, 338 deselected in 77.00s (0:01:16)`, exit 0, no skip/xfail. It includes the 25 synthetic cases and the nine stresses. Separate review of the fixes concluded without open findings after a red/green oracle-drift regression.

## 2B — persistence and semantic checks

Seven initial red regressions reproduce an inherited lock, a document without targets, absent resources and unchecked families/arms. Red regressions added for bool/float seeds, corrupted sums on resume, missing/duplicated/negative resource measurements or ones with ambiguous units, and JSON with duplicate keys. The reader now checks exact schemas, keys and counts, corpus/budget denominators and masses; it reconstructs from C0 also sums and valid/null counts of L_resolved and unseen sums. The CE tolerance is 1e-9 bits/target (§6.5); diagnostics and mass conservation use 1e-12 per position for numerical accumulation. Keys and counts remain exact.

Empty document/band rows are produced and reconstructed using all the held-out documents, with zero sums and nulls with their reason in the report. The previous negative test now corrupts the result explicitly: it keeps the refusal of the omission without requiring the producer to keep omitting the rows.

Fit and evaluation times in seconds from `time.perf_counter`; RSS in bytes from `resource.getrusage(RUSAGE_SELF).ru_maxrss`, the historical maximum of the process observed per model, not an isolated measurement of the allocation of the single model. All measurements are in `metadata`, excluded from identity, partitions and deterministic tables. No forecast of the campaign.

R1 now keeps both empirical and smoothed frequencies beside the counts (§8.3), without changing the JSD. Reviews of the changes, separate from the writing, flagged and had covered also the completeness of the resource metadata. No real fit.

2B closure: `uv run pytest -q tests/test_v31_report_semantics.py tests/test_v31_completion.py tests/test_v31_descriptive.py --tb=short` → `86 passed in 17.65s`; `uv run pytest -m v31 -q` → `302 passed, 338 deselected in 82.57s (0:01:22)`, exit 0 and zero skip/xfail.

## 2C — evidence in the manifest

Resumption on 22 September after the interruption: no damage (checks in the [handoff](HANDOFF.md)); the uncommitted diff of the sub-stage was consistent (`318 passed, 338 deselected`) and was kept. The test of the recomputed V3 record was run red before the fix (`2 failed, 1 passed`: the two tampered records reached the fit), then green. Inventory: on the complete real collection nothing missing; removing a test, the gate names exactly that test. Commit `482cef0`: `321 passed, 338 deselected`; `642 passed, 17 skipped`.

## 3 — integral review

Independent checks in the [handoff](HANDOFF.md). Fixes, each with a red test first:

- `f3f8a65`, names of the report contract and resources in `model_diagnostics.csv`: `322 passed, 338 deselected`; `643 passed, 17 skipped`.
- `5dc7d1b`, `training`/`fragments` recomputed from the ledger and observed nodes (§9.1): `324 passed, 338 deselected`; `645 passed, 17 skipped`.
- `0a6f644`, complete report tables and regeneration comparison §12.2: `328 passed, 338 deselected`; `649 passed, 17 skipped`.

What remained before V3 was the implementation of the five §11.6 figures, because the code identity covers all of `src/hexis`: done in `559dc40` (section 5).

## 4 — closure

On the bytes of the closure commit, code identical to `0a6f644`, final lines verbatim, all exit 0:

```text
uv run --frozen pytest -m v31 -q -p no:cacheprovider
328 passed, 338 deselected in 148.75s (0:02:28)

uv run --frozen pytest -q -p no:cacheprovider
649 passed, 17 skipped in 153.77s (0:02:33)

uv lock --check
Resolved 23 packages in 3ms
```

V2 closed. Stop for review before V3; no push.

## 5 — §11.6 figures

Signatures approved by the owner, text of the figures in English, SVGs produced by `run_report` from the same verified tables. New tests red on the previous code (`4 failed`), then green; figures of the fixture inspected visually and corrected for readability. Also corrected the serialization of `model_diagnostics.csv`, which wrote the support histogram as a Python repr. Commit `559dc40`, final lines verbatim, all exit 0:

```text
uv run --frozen pytest -m v31 -q -p no:cacheprovider
332 passed, 338 deselected in 162.20s (0:02:42)

uv run --frozen pytest -q -p no:cacheprovider
653 passed, 17 skipped in 168.70s (0:02:48)

uv lock --check
Resolved 23 packages in 3ms
```

Stop for review before V3; no push.
