# HORMATHOS documents — a reading guide (deposited design 3.1)

Start from the [README](../README.md). The [introduction to this folder](README.md) groups the documents by kind; this guide gives each one a line. Then, by what you need:

| Document | What it is | Read it if… |
|---|---|---|
| [RESULTS.md](RESULTS.md) | Statement of results and limitations: every term defined, every number traced to its table | you want the findings and what they do not show |
| [../results/README.md](../results/README.md) | Guide to the published tables, figures, logs and archives | you want the data |
| [Deposited plan 3.1, English](contracts/hexis-3.1-en/HEXIS_piano_definitivo_v3.1_2026-09-15.md) | The research design, fixed before the campaign; the [Italian original](contracts/hexis-3.1/HEXIS_piano_definitivo_v3.1_2026-09-15.md) and its JSON contracts govern, identified by [V3-001-deposit.json](V3-001-deposit.json) | you want to judge the method |
| [02_DECISION_LOG.md](02_DECISION_LOG.md) | Every decision since the design: V3-001 adopts it, V3-002 realigns the repository and sets the licences, V3-003 names the project, V3-004–V3-006 close the reviews, V3-007 publishes the results, V3-008 extends the name HORMATHOS to the reader-facing texts and the release, V3-009 adds the figures for reading, V3-010 rewrites the reader-facing texts without internal references, V3-011 gives every folder an introduction, V3-012 gives the archive its guide and replaces the Italian texts outside the deposit with their English translation, V3-013 makes a last reading of the reader-facing texts so that every term they use is explained. V3-001 and V3-002 are given in English; their Italian originals, which govern, are kept at the tag `hormathos-v5-evidence` | you want to know why something is as it is |
| [01_MASTER_SPEC.md](01_MASTER_SPEC.md) | One-page statement of authority and perimeter | you are checking what governs what |
| [03_ROADMAP.md](03_ROADMAP.md) | The six phases of the work, V0 (deposit and set-up) to V5 (report), with their commits and status | you want the timeline |
| [HANDOFF.md](HANDOFF.md) | Technical record: runs, commands, checks, reviews, identities, dated newest first | you want to verify or reproduce a step |
| [TEST_INVENTORY.md](TEST_INVENTORY.md) | Map from each obligation of the design to the test that enforces it | you want to know what the tests guarantee |
| [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) | Active sources | you want the references |
| [04_AI_HANDOFF_PROMPT.md](04_AI_HANDOFF_PROMPT.md) | Standing instructions for the AI coding assistants, copied to `CLAUDE.md` and `AGENTS.md` | you want to see how the assistants were constrained |

The [contracts/](contracts/) folder holds the deposit byte for byte (`hexis-3.1/`, Italian, normative) and its non-normative English companions (`hexis-3.1-en/`, V3-003), each opening with the SHA-256 of its original. The [archive](../archive/README.md) keeps the earlier design v2.1 with the records of its checkpoints, an alternative implementation of the model (`candidates/`), the retired statistical tests, the previous research proposal and the corpus audit of 4 September 2026, as they were at `5f1ec06`, byte for byte or, for the texts written in Italian, in English translation (V3-012): a record, not an executable tree and not a competing authority; the status of each item is in V3-002 and in the archive's guide. The new research proposal that section 17.1 of the plan calls for has not been deposited yet.
