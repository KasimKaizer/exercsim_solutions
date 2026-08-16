"""Function for implementing the RNA Transcription exercise on Exercism.org"""

#: Mapping of DNA nucleotides to their RNA complements.
DNA_TO_RNA: dict[int, int] = str.maketrans("ACGT", "UGCA")


def to_rna(dna_strand: str) -> str:
    """Convert a DNA strand to its RNA complement.

    :param dna_strand: The DNA sequence to transcribe.
    :return: The transcribed RNA sequence (unknown bases are left unchanged).
    """
    return dna_strand.translate(DNA_TO_RNA)
