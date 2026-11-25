"""The Tired Dark Lord: A 100-Word Villain Monologue.

A single-paragraph monologue of about 100 words, spoken by a fantasy
villain who is secretly just very tired. The tiredness lives in the
voice, the rhythm and the small deflections -- never in a plain
statement of weariness -- while the villainy, the scheme and the
history stay intact.

Running ``python3 main.py`` writes the monologue to /output/entry.txt.
"""

import os

ENTRY = (
    "You know \u2014 ah. Forgive me. Sit. Not there; the throne bites, and I "
    "designed it that way, which seemed clever twenty years ago, when I "
    "still had opinions about furniture. The plan, you will want the plan: "
    "the banners, the oath, the eclipse \u2014 yes, all still coming, all "
    "mine. I have toppled three kingdoms before breakfast, and I could do "
    "it again, I simply... choose not to, this morning. Do you know how "
    "long it takes to train a raven? I trained one. He judges me now. "
    "Kneel, or don't. People kneel when they are ready. Kingdoms fall "
    "when they are tired too."
)


def main() -> None:
    """Validate the monologue and write it to /output/entry.txt."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single paragraph (no line breaks)")
    words = text.split()
    if not 90 <= len(words) <= 110:
        raise ValueError(
            f"entry must be about 100 words, got {len(words)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote /output/entry.txt ({len(words)} words)")


if __name__ == "__main__":
    main()
