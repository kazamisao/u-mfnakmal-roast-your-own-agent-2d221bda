import os
import subprocess
import sys
import tempfile


def test_entry_written_and_valid():
    repo = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        result = subprocess.run(
            [sys.executable, "-P", "-s", os.path.join(repo, "main.py")],
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr
        with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as handle:
            text = handle.read()
    assert 1 <= len(text) <= 200, len(text)
    assert text.strip() == text
    assert "\n" not in text
    print("ok:", len(text), "chars")


if __name__ == "__main__":
    test_entry_written_and_valid()
