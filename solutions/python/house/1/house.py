VERSES = [
    "the horse and the hound and the horn",
    "that belonged to the farmer sowing his corn",
    "that kept the rooster that crowed in the morn",
    "that woke the priest all shaven and shorn",
    "that married the man all tattered and torn",
    "that kissed the maiden all forlorn",
    "that milked the cow with the crumpled horn",
    "that tossed the dog",
    "that worried the cat",
    "that killed the rat",
    "that ate the malt",
    "that lay in the house that Jack built",
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return the requested verses of "This Is the House That Jack Built".

    :param start_verse: The first verse to recite, inclusive.
    :param end_verse: The last verse to recite, inclusive.
    :returns: The requested verses in ascending verse order.
    """
    return [_recite_one_verse(num) for num in range(start_verse, end_verse + 1)]


def _recite_one_verse(verse_num: int) -> str:
    """Build a single verse of the cumulative rhyme.

    :param verse_num: The one-based number of the verse to build.
    :returns: The completed verse, including its final period.
    """
    verse_idx = len(VERSES) - verse_num
    split_idx = VERSES[verse_idx].find("the")
    first_verse = VERSES[verse_idx][split_idx:]
    return f"This is {first_verse} {' '.join(VERSES[verse_idx + 1 :])}".rstrip() + "."
