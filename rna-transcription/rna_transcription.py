def to_rna(dna_strand):
    rna_strand = ''
    rna_complement = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U" 
    }
    for nucleotides in dna_strand:
        rna_strand = rna_strand + rna_complement[nucleotides]

    return rna_strand

if __name__ == "__main__":
    print(to_rna("ATCG"))
