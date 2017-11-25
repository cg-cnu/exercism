def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError
    return len(filter(lambda (x, y): x != y, zip(strand_a, strand_b)))
