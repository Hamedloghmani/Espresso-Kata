"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
development and functioning of living organisms.
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of
the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or
there is no DNA at all (again, except for Haskell).
Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""


def DNA_strand(dna: str):
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([complements[x] for x in dna])
