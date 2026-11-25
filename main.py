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
    "Come in, come in \u2014 mind the third step, it sighs. Yes, I am the "
    "Dark Lord. No, the cape is not dramatic; it is warm, and the castle is "
    "freezing, and the heating minions unionised in spring. The prophecy says "
    "a hero will end me at dawn. Dawn was four hours ago, and three of you "
    "have already knocked \u2014 one asked for directions, one wanted a selfie, "
    "one brought a r\u00e9sum\u00e9. I have conquered nine realms, and none of them "
    "had decent tea. Sit down, hero. The throne is taken; I claimed it first, "
    "and it is the only chair with a cushion."
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
