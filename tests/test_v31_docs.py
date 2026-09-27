"""V0 authority, preserved history and declared operational limits."""
import hashlib
import json
import subprocess
from pathlib import Path

import pytest

pytestmark = pytest.mark.v31
ROOT = Path(__file__).resolve().parents[1]

# The three V3-001 blocks are the acts of 16, 17 and 22 September: V3-002 supersedes
# sentences of theirs, it never rewrites their bytes. The hash starts at the first
# V3-001 heading: the file title is not an act and follows the project name (V3-003).
# Since V3-012 the log holds their English translation; the Italian originals, which
# govern, keep these hashes at the tag ORIGINALS_TAG.
V3_001_SHA256 = '8ee0f130ac59085862c940c0804fc25733a7a12f9e83bb0abf95c18c9fba8864'
V3_002_SHA256 = '094a686e52841202b7185d383f48f1e8619e8ae11db934ea61a6966b7d01c5ed'
ORIGINALS_TAG = 'hormathos-v5-evidence'
LOCK_SHA256 = '33db43b00bcb21ab12aedf6dcc4257764770bff0115dc0d1dfab6e5ea89876bf'
REALIGNMENT_BASE = '5f1ec06afa192c8d0f006d7f39cdb97df72c2983'
# V3-012: the archived Italian texts are read in English, each at the path of its original
# unless named otherwise here (archived path -> path at the base). Their originals stay at
# the base, tagged archive/pre-realign; each translation names their SHA-256 in its header.
# ARCHIVE_GUIDE is the only file of the archive that has no original.
ARCHIVE_GUIDE = 'archive/README.md'
ARCHIVE_TRANSLATIONS = {
    'archive/README_at_5f1ec06.md': 'README.md',
}


def _git(*argv, stdin=None, text=True):
    return subprocess.run(['git', *argv], cwd=ROOT, input=stdin, check=True,
                          capture_output=True, text=text).stdout


def _declared_original_sha256_in(text):
    """The SHA-256 a translation names for its original, in its opening header."""
    import re
    found = re.search(r'SHA-256[^`]{0,40}`([0-9a-f]{64})`', text[:1500])
    assert found, text[:80]
    return found.group(1)


def _declared_original_sha256(path):
    return _declared_original_sha256_in(path.read_text())


def test_active_authority_and_instructions_are_aligned():
    for name in ['README.md', 'AGENTS.md', 'CLAUDE.md', 'docs/01_MASTER_SPEC.md',
                 'docs/02_DECISION_LOG.md', 'docs/03_ROADMAP.md',
                 'docs/00_INDEX.md', 'docs/HANDOFF.md']:
        text = (ROOT/name).read_text()
        assert 'V3-001' in text and 'V3-002' in text and 'V3-003' in text, name
        assert '3.1' in text, name
    readme = (ROOT/'README.md').read_text()
    # Retired on 2026-09-24 (V3-005): this test pinned the V2-phase sentence "V0–V2 completed;
    # V3–V5 not attested; no real fit has ever been run", false since V3. A phase sentence would
    # go stale again in V4 while the tests stay frozen, so the pin is replaced by properties
    # true in every phase: the status defers to the handoff and never denies the real fits.
    status = readme.partition('## Status')[2].partition('\n## ')[0]
    assert '(docs/HANDOFF.md)' in status
    assert 'no real fit has ever been run' not in readme
    assert 'archive/' in readme
    assert 'Stop for review before V3.' in (ROOT/'docs/HANDOFF.md').read_text()


def test_the_v3_001_and_v3_002_originals_are_preserved_and_bound_to_their_translation():
    """Retired on 2026-09-27 (V3-012): this test pinned the Italian V3-001 blocks in the log,
    which now holds their English translation. The property that no byte of the acts is lost
    moves to Git: at the tag the Italian blocks keep their hashes, and the English text of
    each act in the log names the hash of its original."""
    def acts(log):   # headings only: the notes of the translations quote them in backticks
        start = {n: log.index(f'\n## V3-00{n} —') + 1 for n in (1, 2, 3)}
        return {'V3-001': log[start[1]:start[2]], 'V3-002': log[start[2]:start[3]]}
    original = _git('show', f'{ORIGINALS_TAG}:docs/02_DECISION_LOG.md')
    assert 'V3-002 — Riallineamento della repository' in original
    expected = {'V3-001': V3_001_SHA256, 'V3-002': V3_002_SHA256}
    for act, text in acts(original).items():
        assert hashlib.sha256(text.encode()).hexdigest() == expected[act], act
    for act, text in acts((ROOT/'docs/02_DECISION_LOG.md').read_text()).items():
        assert _declared_original_sha256_in(text) == expected[act], act
        assert 'Riallineamento' not in text, act


def test_the_package_is_hormathos_and_hexis_names_only_the_design():
    """V3-003: the project and its package are HORMATHOS; `hexis` survives only as the
    name of the deposited design and in its identifiers, never as a package."""
    import importlib.util
    assert importlib.util.find_spec('hexis') is None
    assert not (ROOT/'src/hexis').exists()
    spec = importlib.util.find_spec('hormathos')
    assert spec is not None and Path(spec.origin).resolve() == ROOT/'src/hormathos/__init__.py'


def test_the_deposit_and_the_lock_are_byte_preserved():
    record = json.loads((ROOT/'docs/V3-001-deposit.json').read_text())
    for name, sha in record['files'].items():
        assert hashlib.sha256((ROOT/record['root']/name).read_bytes()).hexdigest() == sha, name
    assert hashlib.sha256((ROOT/'uv.lock').read_bytes()).hexdigest() == LOCK_SHA256


def test_the_sdist_ships_exactly_the_tracked_tree():
    """The sdist is a closed list equal to the tracked tree (V3-003, R1): the proposal drafts,
    the local scripts and the tools' notes stay out of any distribution. Hatchling honours
    only the root .gitignore, so an untracked file must not sit under a listed path either."""
    import tomllib
    targets = tomllib.loads((ROOT/'pyproject.toml').read_text())['tool']['hatch']['build']['targets']
    listed = targets['sdist']['only-include']

    def files(*argv):
        out = subprocess.run(['git', 'ls-files', '-z', *argv], cwd=ROOT, check=True,
                             capture_output=True, text=True).stdout
        return [path for path in out.split('\0') if path]

    def under(path, entry):
        return path == entry or path.startswith(entry + '/')

    tracked = files()
    assert tracked and len(set(listed)) == len(listed)
    for path in tracked:
        assert any(under(path, entry) for entry in listed), path
    for entry in listed:
        assert any(under(path, entry) for path in tracked), entry
    for path in files('--others', '--exclude-standard'):
        assert not any(under(path, entry) for entry in listed), path

def test_all_preserved_v21_documents_match_the_original_hash_inventory():
    history = ROOT/'archive/docs/history/v2.1'
    records = json.loads((history/'SHA256SUMS.json').read_text())
    assert len(records) == 10
    for name, record in records.items():
        path = history/name
        if str(path.relative_to(ROOT)) in ARCHIVE_TRANSLATIONS:   # V3-012: read in English
            assert _declared_original_sha256(path) == record['sha256'], name
        else:
            assert hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'], name


def test_the_archive_is_a_record_and_never_a_dependency():
    """`archive/` keeps the history at its own paths; nothing active imports it and
    no archived test is collected (plan §13.1, items 4–5; V3-002)."""
    archive = ROOT/'archive'
    assert (archive/'README.md').is_file()
    for expected in ['src/hexis/stats/permutation.py', 'src/hexis/registry.py',
                     'src/hexis/pipeline/legacy_audit.py', 'tests/test_run_audit.py',
                     'docs/history/v2.1/02_DECISION_LOG.md', 'candidates/README.md']:
        assert (archive/expected).is_file(), expected
    assert not (ROOT/'src/hormathos/stats').exists()


def test_every_archived_file_has_its_bytes_at_the_base():
    """Rule `archive/P` (V3-002): every archived file holds the bytes `P` had at the
    base, so nothing new can sit in the archive under a historical name. V3-012 admits
    the guide and the declared English translations: each names in its header the SHA-256
    of its original, whose bytes the base keeps, so no historical byte is lost."""
    base = {}
    for entry in _git('ls-tree', '-r', '-z', REALIGNMENT_BASE).split('\0'):
        if entry:
            meta, path = entry.split('\t', 1)
            base[path] = meta.split()[2]
    archived = [path for path in _git('ls-files', '-z', 'archive').split('\0') if path]
    blobs = _git('hash-object', '--stdin-paths', stdin='\n'.join(archived)).split()
    assert archived and len(blobs) == len(archived)
    assert ARCHIVE_GUIDE in archived and set(ARCHIVE_TRANSLATIONS) <= set(archived)
    for path, blob in zip(archived, blobs):
        if path == ARCHIVE_GUIDE:
            continue
        if path in ARCHIVE_TRANSLATIONS:
            original = _git('cat-file', 'blob', base[ARCHIVE_TRANSLATIONS[path]], text=False)
            assert blob != base[ARCHIVE_TRANSLATIONS[path]], path
            assert _declared_original_sha256(ROOT/path) == hashlib.sha256(original).hexdigest(), path
            continue
        assert base.get(path.removeprefix('archive/')) == blob, path


def test_test_inventory_explicitly_tracks_future_obligations():
    text = (ROOT/'docs/TEST_INVENTORY.md').read_text()
    for index in range(1, 31):
        assert f'T{index:02d}' in text
    assert 'PENDING' in text
    assert 'inventory_only' in text
    assert 'test_bootstrap_holm.py' in text


def test_pipeline_does_not_import_candidates_or_inferential_utilities():
    import ast
    for path in (ROOT/'src/hormathos').rglob('*.py'):
        tree = ast.parse(path.read_text())
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.append(node.module or '')
        assert not any(name.startswith(('candidates', 'archive', 'hormathos.stats'))
                       for name in imports), path


def test_the_three_standing_instruction_copies_are_identical():
    """The template in 04 is the source; CLAUDE.md and AGENTS.md are its copies,
    and AGENTS.md may differ only in its first line."""
    template = (ROOT/'docs/04_AI_HANDOFF_PROMPT.md').read_text()
    fenced = template.partition('````markdown\n')[2].partition('\n````')[0] + '\n'
    claude = (ROOT/'CLAUDE.md').read_text()
    agents = (ROOT/'AGENTS.md').read_text()
    assert fenced == claude
    assert agents.splitlines(keepends=True)[1:] == claude.splitlines(keepends=True)[1:]
