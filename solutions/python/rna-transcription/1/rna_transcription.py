"""Function for implementing the RNA Transcription exercise on Exercism.org"""

# Mapping of DNA nucleotides to their RNA complements.
DNA_TO_RNA: dict[str, str] = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand: str) -> str:
    """Convert a DNA strand to its RNA complement.

    :param dna_strand: The DNA sequence to transcribe.
    :return: The transcribed RNA sequence (unknown bases are skipped).
    """
    return "".join(DNA_TO_RNA.get(base, "") for base in dna_strand)
