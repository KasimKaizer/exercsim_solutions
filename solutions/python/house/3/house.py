"""Function for implementing the House exercise on Exercism.org"""

#: Cumulative rhyme fragments, ordered from house to horse.
RHYME_PARTS: tuple[str] = (
    "the house that Jack built",
    "the malt that lay in",
    "the rat that ate",
    "the cat that killed",
    "the dog that worried",
    "the cow with the crumpled horn that tossed",
    "the maiden all forlorn that milked",
    "the man all tattered and torn that kissed",
    "the priest all shaven and shorn that married",
    "the rooster that crowed in the morn that woke",
    "the farmer sowing his corn that kept",
    "the horse and the hound and the horn that belonged to",
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return the requested verses of "This Is the House That Jack Built".

    :param start_verse: The first verse to recite, inclusive.
    :param end_verse: The last verse to recite, inclusive.
    :returns: The requested verses in ascending verse order.
    """
    return [_recite_one_verse(num) for num in range(start_verse, end_verse + 1)]


def _recite_one_verse(verse_num: int) -> str:
    """Build a verse by joining its cumulative rhyme fragments.

    :param verse_num: The one-based number of the verse to build.
    :returns: The completed verse, including its final period.
    """
    return f"This is {' '.join(verse for verse in RHYME_PARTS[verse_num - 1 :: -1])}."
