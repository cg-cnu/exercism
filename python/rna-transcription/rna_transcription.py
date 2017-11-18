def to_rna(dna_strand):
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    try:
        set(mapping.keys) == set(dna_strand)
    except:
        raise ValueError

    map(dna_strand.replace,        )