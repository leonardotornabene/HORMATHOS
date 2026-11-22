# HORMATHOS results

The finished results of the HORMATHOS study, published by entry V3-007 of the [decision log](../docs/02_DECISION_LOG.md). The [statement of results and limitations](../docs/RESULTS.md) reads them and defines every term; this page says what each file is. Apart from the pages that describe the files (this one, the [figure gallery](figures/README.md) and the [guide to the run folders](hexis31/README.md)), every file here is byte for byte the one that the pipeline, a check or the figure script wrote; nothing was edited for publication.

The directory name `hexis31/` comes from HEXIS 3.1, the working title of the research plan when the data were produced; the manifests record these paths, so they are kept.

## The final campaign: `hexis31/v3-seed0-v3006/`

Run ID `6aa1b719e274116c5660790cf9b2ad73c7e1853cec672688e1dc27d6b7d60e05`: 490 train–score pairs and 980 models in six analysis settings, repeated with seeds (random draws of the training sample and of the shuffle) 0–19 in the main setting and 0–9 in the other five. [manifest.json](hexis31/v3-seed0-v3006/manifest.json) (SHA-256 `3243fc329351e45e1d1c2c2f68a5be57fec2ea197ef5a81a170a5c11f4ca6dab`) lists all 931 artifacts with their hashes; the repository holds the ones below, the rest is in the campaign archive.

Scores are in bits per target, a target being a predicted annotation symbol. The *gain* is how many bits the trained model saves over a predictor that knows only symbol frequencies; the *order advantage* Q is the gain in the original order minus the gain after shuffling the symbols within each sentence. The files use short codes for settings, blocks, groups and conditions; [Reading the source tables](../docs/RESULTS.md#reading-the-source-tables) maps each code to its name.

| File | Content |
|---|---|
| [seed_summaries.csv](hexis31/v3-seed0-v3006/seed_summaries.csv) | mean, standard deviation (SD), minimum and maximum over seeds of every quantity, per setting, block, document and group: the main table |
| [contrasts.csv](hexis31/v3-seed0-v3006/contrasts.csv) | hexameter and prose averages and their difference, per setting, seed and way of averaging |
| [sensitivity_pairs.csv](hexis31/v3-seed0-v3006/sensitivity_pairs.csv) | each variant minus the main setting on the same seed |
| [block_pairs.csv](hexis31/v3-seed0-v3006/block_pairs.csv), [document_scores.csv](hexis31/v3-seed0-v3006/document_scores.csv) | loss sums per held-out block and per document, original and shuffled, every seed |
| [aggregation_weights.csv](hexis31/v3-seed0-v3006/aggregation_weights.csv) | the two ways of averaging and the training shares behind each block |
| [jsd_pairs.csv](hexis31/v3-seed0-v3006/jsd_pairs.csv), [jsd_centroids.csv](hexis31/v3-seed0-v3006/jsd_centroids.csv), [jsd_contributions.csv](hexis31/v3-seed0-v3006/jsd_contributions.csv) | Jensen–Shannon divergences between the symbol frequencies of blocks and groups, and the contribution of each symbol; descriptive only |
| [root_distributions.csv](hexis31/v3-seed0-v3006/root_distributions.csv) | symbol frequencies per block, used by the frequency comparison |
| [model_diagnostics.csv](hexis31/v3-seed0-v3006/model_diagnostics.csv), [arm_diagnostics.csv](hexis31/v3-seed0-v3006/arm_diagnostics.csv), [fragment_diagnostics.csv](hexis31/v3-seed0-v3006/fragment_diagnostics.csv) | contexts stored by the models, weights given to each context length, unseen symbols and training fragments |
| five `figure__*.svg` | the five figures produced by the pipeline: [corpus](hexis31/v3-seed0-v3006/figure__corpus_annotation.svg), [profiles](hexis31/v3-seed0-v3006/figure__block_document_profiles.svg), [sensitivities](hexis31/v3-seed0-v3006/figure__sensitivities_two_weights.svg), [annotation frequencies](hexis31/v3-seed0-v3006/figure__R1.svg), [supports and weights](hexis31/v3-seed0-v3006/figure__supports_mixture_masses.svg); to read them, use the [figure gallery](figures/README.md) |
| `tree_validation.json`, `v31_process.json`, `v31.junit.xml` | the evidence that this code passed its checks: the battery of synthetic cases and the 431-test acceptance run |

[`hexis31/v3-seed0-v3006-regeneration/`](hexis31/v3-seed0-v3006-regeneration/manifest.json) is the separately executed regeneration of seed 0: 70 of 70 compared artifacts identical.

## Figures for reading: `figures/`

The [figure gallery](figures/README.md) redraws the five figures one panel at a time, full width, from the published tables alone, with a short explanation beside each panel. The five pipeline figures above stay the canonical ones; [`make_figures.py`](figures/make_figures.py) reproduces them byte for byte before it draws.

## Other published material

- [`hexis31/v1/`](hexis31/v1/): the encoded corpus, the input of every run: documents, audit tables, encoded sentences and their coordinates in the source.
- [`hexis31/v3-seed0-v3006-logs/`](hexis31/v3-seed0-v3006-logs/), [`v4-logs/`](hexis31/v4-logs/), [`v5-logs/`](hexis31/v5-logs/): the logs, commands and independent check scripts of three stages: the acceptance checks and seed 0 of every setting with its regeneration; the verification of the full campaign run; the report and the final checks. Each directory's `commands.txt` gives the commands verbatim. The terminal log of the full campaign run was lost, as [its record](hexis31/v4-logs/01-v4-resume-log-lost.txt) states.
- [`hexis31/v3-005-review/`](hexis31/v3-005-review/): the mutation check of the review before the campaign: 18 deliberately broken versions of the code, all 18 caught by the checks.

The logs are verbatim, so they use the project's internal names. Local paths in them (`/Users/…`, `/tmp/…`) are those of the author's machine, and sentences such as "Git-ignored, not deposited" describe their status before publication.

## Complete archives

The [GitHub Release `hormathos-v5-evidence`](https://github.com/leonardotornabene/HORMATHOS/releases/tag/hormathos-v5-evidence) holds what is too large for the repository. The checksums below let anyone confirm that a download is intact.

| Archive | SHA-256 | Content |
|---|---|---|
| `hormathos-campaign-v3006.tar.gz` (45 MB) | `3dadf6cecc303281897995b84c479721ce56e304859456f18dd9abb0164bec10` | `v1`, `v3-seed0-v3006` complete (490 pair records, 280 sample ledgers — which sentences each training sample took — and 140 position vectors — the loss at every scored position of the main setting) and its regeneration |
| `hormathos-superseded-runs.tar.gz` (17 MB) | `1a4fbf43b021dd442285927e8a76e687d905020220d2a29e9c4931f368a42cc3` | earlier runs, superseded by the two reviews before the campaign and never resumed: `v1-development`, `v1-reproduction`, `v2-pre-v3-audit-2026-09-24`, `v3-seed0`, `v3-seed0-r4-r6`, their regenerations and logs |

## Reproduce the published campaign

Start in a separate checkout of `hormathos-v5-evidence` (commit `9814871`) and install the locked environment:

```bash
git clone https://github.com/leonardotornabene/HORMATHOS.git hormathos-v5
cd hormathos-v5
git switch --detach hormathos-v5-evidence
uv sync --frozen --python 3.12.13
```

### Verify the release files

Save `hormathos-campaign-v3006.tar.gz` from the [release](https://github.com/leonardotornabene/HORMATHOS/releases/tag/hormathos-v5-evidence) in the parent directory of the checkout. Run these commands from the checkout root:

```bash
archive=../hormathos-campaign-v3006.tar.gz
digest=3dadf6cecc303281897995b84c479721ce56e304859456f18dd9abb0164bec10
printf '%s  %s\n' "$digest" "$archive" | shasum -a 256 -c - &&
  mkdir -p results/hexis31 &&
  tar -xzf "$archive" -C results/hexis31
```

Then validate the three extracted directories:

```bash
uv run --no-sync python - <<'PYTHON'
from pathlib import Path

from hormathos.pipeline import corpus_run, scientific_run

runs = Path("results/hexis31")
for name, validate in (
    ("v1", corpus_run.validate_run),
    ("v3-seed0-v3006", scientific_run.validate_run),
    ("v3-seed0-v3006-regeneration", scientific_run.validate_run),
):
    print(name, len(validate(runs / name)["artifacts"]))
PYTHON
```

The expected counts are 9 corpus artifacts, 931 campaign artifacts and 73 regeneration artifacts. This checks the saved files against their manifests. The published regeneration covers seed 0 and includes 70 artifacts compared with the campaign. Use `validate_run` in automation to get an error exit status when a validation fails. The V5 log also lists the historical diagnostic [report_checks.py](hexis31/v5-logs/report_checks.py).

### Rerun the experiment

From the same clean checkout, [fetch the three pinned Greek CoNLL-U files](../data/README.md#getting-the-corpus) into `data/raw/UD_Ancient_Greek-Perseus`. The V2 acceptance tests read them even when the campaign uses the encoded corpus from the archive. Use one encoded corpus directory for both new runs. Keep it read-only during validation, fitting and report generation, and let only one process write to each output directory. The report reads `audit_contingency.csv` again when it draws the corpus figure, so that file must remain stable too.

The commands below use `results/hexis31/v1`. The acceptance suite reads V1 at that path from the checkout root. To rebuild V1 in a clean checkout without extracting the archive, run `hormathos.pipeline.run_audit` and then `hormathos.pipeline.run_encode` with `--config config/default.yaml`, `--data-root data/raw/UD_Ancient_Greek-Perseus` and `--output-dir results/hexis31/v1`.

Choose two unused output directories. The release campaign already contains its final report and is closed. Use `--resume` to extend your own validated seed-0 run.

```bash
(
  set -eu

  config=config/default.yaml
  corpus=results/hexis31/v1
  campaign=results/hexis31/reproduction-v5
  regeneration=results/hexis31/reproduction-v5-seed0

  for output in "$campaign" "$regeneration"; do
    uv run --no-sync python -m hormathos.pipeline.run_tree_validation \
      --config "$config" --corpus-dir "$corpus" --output-dir "$output"
    uv run --no-sync python -m hormathos.pipeline.run_descriptive \
      --config "$config" --corpus-dir "$corpus" --output-dir "$output" --cell all --seed 0
  done

  uv run --no-sync python -m hormathos.pipeline.run_descriptive \
    --config "$config" --corpus-dir "$corpus" --output-dir "$campaign" --cell all --resume
  uv run --no-sync python - "$campaign" "$regeneration" <<'PYTHON'
import json
from pathlib import Path
import sys

campaign, regeneration = map(Path, sys.argv[1:])
expected = {path.name for path in campaign.glob("pair__*__s0.json")}
actual = {path.name for path in regeneration.glob("pair__*__s0.json")}
if len(expected) != 42 or actual != expected:
    raise SystemExit("Expected the same 42 seed-0 pair records in both runs.")

mismatches = []
for name in sorted(expected):
    original = json.loads((campaign / name).read_bytes())
    regenerated = json.loads((regeneration / name).read_bytes())
    for arm in ("original", "shuffled"):
        left = original["models"][arm]["fingerprint"]
        right = regenerated["models"][arm]["fingerprint"]
        if left != right:
            mismatches.append(f"{name} ({arm}): {left} != {right}")
if mismatches:
    raise SystemExit("Assess these model fingerprint differences before acceptance.\n"
                     + "\n".join(mismatches))
print("All 84 seed-0 model fingerprints match.")
PYTHON
  uv run --no-sync python -m hormathos.pipeline.run_report \
    --config "$config" --corpus-dir "$corpus" --output-dir "$campaign" \
    --regenerated-dir "$regeneration"
)
```

The fingerprint check before `run_report` implements the review step required by [V3-005(d)](../docs/02_DECISION_LOG.md#v3-005--closure-of-the-v3-review-and-re-attestation-of-v2-and-seed-0-2026-09-24). If any fingerprint differs, assess the listed differences before accepting the regeneration. The report then checks the independent seed-0 run under the deposited comparison rules. Keys and counts must match exactly. The tolerance for a loss sum is `n × 10⁻⁸` bits for `n` eligible targets. See [the campaign handoff](../docs/HANDOFF.md#campaign-v4-and-report-v5--24-and-25-september-2026) for the original execution record.

## Licence

Everything here derived from the corpus — the encoded corpus, tables, figures, manifests, pair records, ledgers and position vectors — is under CC BY-NC-SA 2.5, the licence of its source, UD Ancient Greek Perseus r2.18 (commit `37837c7a3c592c9563f8c51cc63344b87247f8a5`) and the Ancient Greek Dependency Treebank (AGDT/Perseus). Logs and this page are CC BY 4.0, except the corpus-derived values they quote; check scripts are MIT. The licence decisions are entries V3-002 and V3-007 of the [decision log](../docs/02_DECISION_LOG.md).
