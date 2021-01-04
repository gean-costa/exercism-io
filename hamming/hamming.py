def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The length of DNA strands must be equal.")

    d = sum([a != b for a, b in zip(strand_a, strand_b)])

    return d
