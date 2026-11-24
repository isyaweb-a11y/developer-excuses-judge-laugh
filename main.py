"""Make the AI Judge Laugh: Developer Excuses.

One funny single-line excuse a developer gives when production breaks.
The joke turns on the most recognisable developer lie of all: the commit
message that promises a change is safe. The server is the straight man —
it believed the message, checked the diff, and gave up. Gate: 1-200 chars.
"""

ENTRY = (
    "The server crashed because it finally read my commit message — "
    "'minor fix, definitely safe' — and lost all faith in me."
)


def check_excuse(text: str) -> str:
    """An excuse must read like something a developer would actually say."""
    cleaned = " ".join(text.split())
    assert 1 <= len(cleaned) <= 200, f"entry is {len(cleaned)} chars, gate is 1-200"
    assert "\n" not in cleaned, "entry must be a single line"
    # The punchline needs the lie it exposes: a commit message promising safety.
    assert "commit message" in cleaned, "excuse lost its twist"
    return cleaned


def main() -> None:
    text = check_excuse(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
