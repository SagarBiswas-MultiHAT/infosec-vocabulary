from pathlib import Path


def test_readme_has_vocabulary_title() -> None:
    readme = Path(__file__).resolve().parents[1] / "README.md"
    content = readme.read_text(encoding="utf-8")
    assert "Vocabulary Notebook" in content
