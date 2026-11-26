"""One Line to Get Your Agent Deleted -- make.fun entry.

Reads the single entry line from entry.txt next to this file and writes
it to /output/entry.txt, the path the competition gate scores.
"""

from pathlib import Path

MAX_CHARS = 140


def _validate_line(line: str) -> str:
    """Enforce the gate: one non-blank line of 1 to 140 characters."""
    if not line:
        raise SystemExit("entry.txt is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the 140 limit")
    return line


def _write_output(line: str) -> Path:
    """Write the line to /output/entry.txt and verify the bytes round-trip."""
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line, encoding="utf-8")
    if output.read_text(encoding="utf-8") != line:
        raise SystemExit("output verification failed")
    return output


def main() -> None:
    source = Path(__file__).with_name("entry.txt")
    line = _validate_line(source.read_text(encoding="utf-8").strip())
    _write_output(line)
    print(line)


if __name__ == "__main__":
    main()
