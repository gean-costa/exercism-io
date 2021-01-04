codons_proteins = {
    "AUG": 'Methionine',
    "UUU": 'Phenylalanine',
    "UUC": 'Phenylalanine',
    "UUA": 'Leucine',
    "UUG": 'Leucine',
    "UCU": 'Serine',
    "UCC": 'Serine',
    "UCA": 'Serine',
    "UCG": 'Serine',
    "UAU": 'Tyrosine',
    "UAC": 'Tyrosine',
    "UGU": 'Cysteine',
    "UGC": 'Cysteine',
    "UGG": 'Tryptophan',
    "UAA": 'STOP',
    "UAG": 'STOP',
    "UGA": 'STOP'
}


def proteins(strand):
    codons = []
    index = 0
    while index < len(strand):
        if codons_proteins[strand[index:index+3]] == 'STOP':
            break
        else:
            codons.append(codons_proteins[strand[index:index+3]])
        index += 3
    return codons
