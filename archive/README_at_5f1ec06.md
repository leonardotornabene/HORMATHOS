> **English translation; the Italian original governs** (V3-012).
> Original: `README.md` at commit `5f1ec06` (tag `archive/pre-realign`), the project's front page before the realignment, kept at `archive/README.md` until V3-012; SHA-256 `41c79416012355b8a9b3e9da81392b6663b60a4a2829deeb5ea6d3b3e3291533`.
> Translated on 2026-09-27. Structure, values and identifiers follow the original; numbers use English notation; link targets are reproduced unchanged and resolve relative to the repository root at `5f1ec06`. Any translator's note is marked *[Translator's note: …]* and changes nothing in the original.

# HEXIS 3.1

Descriptive study of the within-sentence order of the morphosyntactic annotations in the finite Greek corpus UD Perseus r2.18. Decision [V3-001](docs/02_DECISION_LOG.md) adopts the [complete contract](docs/01_MASTER_SPEC.md).

V0–V1 completed and verified: normative deposit, strict configuration, real audit and encoding. The nine artifacts were reproduced byte-for-byte identical in two distinct directories. V2 closed and verified on 22 September 2026, after the reconciliation M1–M5 and the integral review ([handoff](docs/HANDOFF.md)). Evidence on synthetic/analytical fixtures: CTW, sampling/shuffle, scores, diagnostics, R1, scientific persistence and report tables. The five figures of §11.6 are also implemented and verified on fixtures (`559dc40`): the code identity covers all of `src/hexis`, so all the code is written before V3. The integral pre-V3 review of 22 September 2026 made the report validator able to regenerate samples and shuffles without fits, corrected the figures to the real cardinality and made the test inventory exhaustive (`0dc69b5`, [handoff](docs/HANDOFF.md)). Real fits, campaign, report and figures belong to **V3–V5**, not attested. No final result and no new real fit in this tranche.

Operational commands, from the root of the repository (the initial destination must be new):

```bash
uv sync --frozen
uv run python -m hexis.pipeline.run_audit --config config/default.yaml --data-root data/raw/UD_Ancient_Greek-Perseus --output-dir results/hexis31/new-run
uv run python -m hexis.pipeline.run_encode --config config/default.yaml --data-root data/raw/UD_Ancient_Greek-Perseus --output-dir results/hexis31/new-run
```

`run_encode` can also create a new run directly, including the audit. A second start of the same stage is refused. The corpus manifest distinguishes `corpus_complete` from `scientific_complete`; the descriptive stage has its own run with a single manifest, partitions per pair and ledgers identified by their hash. Resumption is verified on synthetic fixtures, including after an interruption between pairs.

The synthetic battery can be run with `uv run python -m hexis.pipeline.run_tree_validation --config config/default.yaml`. The descriptive CLIs accept the deposited configuration; `--fixture` serves only the toy configurations. The selection `--seed 0` is implemented for the future V3 trial, but **this tranche stops for review before V3**. The publication of the V0–V2 evidence in a new scientific run (`run_tree_validation --corpus-dir … --output-dir …`) is implemented and verified on fixtures; on the deposited configuration it is executed at the opening of V3, with the code frozen. The real report requires in the manifest the V2 and V3 evidence, recomputed at every reading, and the regeneration of seed 0 in a distinct directory (`--regenerated-dir`, §12.2).

Python 3.12 via uv, dependencies and lock kept. `uv run pytest -m v31` selects the active acceptance; `uv run pytest` also includes the historical suite and its explicitly pending scaffolds. State attested on the code `0dc69b5` (V2 closure, figures and pre-V3 review): **351 active tests without skip; 672 passed and 17 historical skips in the complete suite**. The historical skips do not attest the new software. [Test inventory](docs/TEST_INVENTORY.md), [roadmap](docs/03_ROADMAP_OPERATIVA_IT.md), [handoff](docs/HANDOFF.md).

The corpus includes 17 censused documents: 11 primary in seven blocks, six inventory only. Merged ADV/PART alphabet, variants 100/105/11. Targets with at least four predecessors in the sentence; source regimes separate from the report group.

v2.1, the PDF proposal and the backup READMEs are historical. The rewriting of the proposal and the publication of the data are separate. The preserved statistical utilities do not enter the descriptive pipeline. The local acquisition script is not a canonical tool.

Code MIT; the raw data remain CC BY-NC-SA 2.5; the legal qualification of the derivatives is not decided in this tranche (§17.3) and no data is published. Raw data immutable/ignored and bulky local results excluded from publication. Do not redistribute the treebanks through this repository. [Active bibliography](docs/BIBLIOGRAPHY.md).
