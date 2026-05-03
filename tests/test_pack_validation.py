"""
Template-pack validator tests for canon #13 — Software Development Lifecycle Framework.

Verifies:
  - README.md + LICENSE present, well-formed
  - 00-github-canonical-pack subfolder exists (the canonical template payload)
  - SDLC source content present
  - No stray junk
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent


class TestRepoStructure:
    def test_readme_exists(self):
        assert (ROOT / "README.md").exists()

    def test_readme_has_h1(self):
        assert (ROOT / "README.md").read_text(encoding="utf-8").strip().startswith("#")

    def test_license_exists(self):
        assert (ROOT / "LICENSE").exists()

    def test_license_is_mit(self):
        c = (ROOT / "LICENSE").read_text(encoding="utf-8")
        assert "MIT License" in c
        assert "Shannon Brian Kelly" in c


class TestCanonicalPack:
    def test_canonical_pack_dir(self):
        """The 00-github-canonical-pack folder is the canonical payload."""
        d = ROOT / "00-github-canonical-pack"
        assert d.exists() and d.is_dir(), "00-github-canonical-pack missing"

    def test_canonical_pack_nonempty(self):
        d = ROOT / "00-github-canonical-pack"
        assert any(d.iterdir()), "canonical pack folder is empty"


class TestSdlcContent:
    def test_sdlc_source_text_present(self):
        """The original SDLC reference text should be in repo root (handles 'life cycle' or 'lifecycle')."""
        all_files = [f.name.lower() for f in ROOT.iterdir() if f.is_file()]
        matched = [n for n in all_files if "life" in n and ("cycle" in n or "ecycle" in n)]
        assert matched, f"no SDLC source file found in root; saw: {all_files}"


class TestRepoCleanliness:
    def test_no_pycache(self):
        assert not (ROOT / "__pycache__").exists()

    def test_no_stray_pyc_files(self):
        pycs = [p for p in ROOT.rglob("*.pyc") if "__pycache__" not in str(p)]
        assert not pycs
