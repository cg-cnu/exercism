def to_rna(dna_strand):
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    if not set(dna_strand) <= set(mapping.keys()):
        raise ValueError
    return "".join([mapping[i] for i in dna_strand])
