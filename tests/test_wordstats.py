import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from wordstats import word_count


def test_word_count():
    assert word_count("The baby is happy very happy now") == 7
