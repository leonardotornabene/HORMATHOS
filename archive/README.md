# archive/ — the project before the deposited plan

This folder keeps the earlier stages of the project: designs, code, tests, documents and results from before 22 September 2026. On that date the repository was realigned to the research plan deposited on 15 September (decision-log entry V3-002). None of it is part of the active study, and none of it governs it. It is kept because it is the record of how the study reached its present form. The decision log and the handoff cite it, and a reader should be able to check what was abandoned and why.

## What you will find

| Path | What it is | Status |
|---|---|---|
| `docs/history/v2.1/` | design **v2.1**, the design before the deposited plan: its specification, decision log (D01–D54), roadmap, handoff and instructions | frozen; its bytes are checked by its `SHA256SUMS.json` |
| `docs/archive_v2_0_pdf/` | the same documents in version 2.0, as PDF | superseded by v2.1 |
| `docs/audit/` | the audit that restored and amended the v2.0 texts into v2.1: record of every edit, changelog, restored specification, proposal D52 | historical |
| `docs/g1_*.md`, `docs/g1_registry_proposal.yaml` | records of the **G1** checkpoint of v2.1: technical ratifications, a proposed registry of documents, proposal D55 (never applied) | historical; they ratify neither the corpus nor the present analysis |
| `docs/HANDOFF.md`, `docs/TEST_INVENTORY.md`, `docs/V2_RECONCILIATION.md` | the technical record, test map and reconciliation register as they stood on 22 September, covering the first phases of the present design | the detailed account that the active decision log cites |
| `docs/implementation/`, `docs/probe_conllu.md` | early implementation plans and a probe of the corpus format | historical |
| `src/hexis/`, `tests/` | retired code of v2.1: the statistical tests (permutation, bootstrap, Holm), the registry and sequence builders, the Latin and confirmatory stages, and their test suites | never imported and never collected by the active project |
| `candidates/` | an alternative implementation of the prediction model, kept in quarantine | never imported |
| `config/history/v2.1/` | the v2.1 configuration | historical |
| `results/` | tables and logs of the corpus audit of 4 September 2026, made under v2.1 | not part of the published results |
| `HEXIS_research_proposal.pdf`, `README_backup.md`, `README_v1_backup.md` | the earlier research proposal and two older front pages | superseded |
| [`README_at_5f1ec06.md`](README_at_5f1ec06.md) | the project's front page just before the realignment, when the project was still called HEXIS | historical |

## What was abandoned

Design v2.1 compared hexameter and prose in Greek and in Latin, and it tested hypotheses with statistical inference: permutation tests with fixed constants, a sign-stability criterion, a sequence of checkpoints G0–G7 and decisions D01–D55. The deposited plan retired all of these. The present study is descriptive, uses the Greek corpus alone and runs no statistical test. The retired elements must not return to the active project: decision-log entry V3-001 lists them, and the active tests check that the retired code stays out of the package.

## Running it

Nothing here runs from the current repository. The paths inside these files, such as `src/hexis`, `docs/01_MASTER_SPEC.md` or `pyproject.toml`, refer to the repository as it was, when they sat at the root. To run or read them in place, check out commit `5f1ec06` (tag `archive/pre-realign`), where every file sits at its original path. Design v2.1 is also fixed by the tag `archive/v2.1`.

## Translations of the Italian texts

Some of these texts were written in Italian. Since decision-log entry V3-012 each of them is replaced here by its English translation, at the same path. A PDF is replaced by a Markdown file with the same name. Every translation opens with a header that names its original and the original's SHA-256. The Italian original keeps governing. It is preserved byte for byte in Git at commit `5f1ec06`, and a test checks each header against those bytes. Apart from this page, every other file here is byte for byte what the same path held at `5f1ec06`.

## Where to go next

- For the active study, see the [README](../README.md) and the [statement of results](../docs/RESULTS.md).
- For why the design changed, see the [decision log](../docs/02_DECISION_LOG.md), entries V3-001 and V3-002.
