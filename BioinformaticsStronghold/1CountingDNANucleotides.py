

def countNumberOfNucleotides(string):
    a_count=0;
    c_count=0;
    g_count=0;
    t_count=0;
    for char in string:
        if char == 'A':
            a_count+=1
        if char == 'C':
            c_count+=1
        if char == 'G':
            g_count+=1
        if char == 'T':
            t_count+=1
    return a_count, c_count, g_count, t_count

print(countNumberOfNucleotides('TCTTTCGTCTCGTATTCTACCTACTTAGACACATACACTTCAAGGTACAGCCCAGCACTCGGAGACTTTGCGACCTGAGTCGACATCGCTGGATCAGGGGAGATGCATGGTCTATGGGATTACCTAGTATGTGGTAAGCATTTCGCGGACACCAAACGGAGTCGTAGTTAATAATAAGAGCGGACACGTTGCCATCTAAATTGGTGGCCTTTAGTTGAATCTTATGCCCCCGTCCTGACTTTGTATAGGTTCTCAACAGTAAATGTTATGCGAACCGTGAGGAAGATTGGACCCAGCTTACTTATTTTTGTGTGTACCTTAACCCCGATACCAAAGTCGAATGTTCAGTTGGCTTGACTAGCTGCGAACATCGAATGGGACCCCTCGAGAGGGAGATCGGTAGGTACTAAGGGTGTTACCGCATAGAAGCCAATGGCTCCCGGTCACTAGGTTATTCGTGACCGCCATGTATCCCTTCCCCTTTGGATGATGTACCACCGCTAAGGGTGCGTCTAATGAGCGTCTATGTTGTCCAAAGGACTGAGTGTGGTGGATTTCTTAATGGCTGGGTTATTGCACGGCTGTAGCTAAGAAATGGGCTCTCTTACCATCAGAATGATGCCCGCGGCTATGACATGGTTTTGTCAGTTGAAGCTTCCACCCCTTCCGGTACGACGTAGCGGTTCTGCGGTGAGATGTTTGTAGCTTCACGAACAATCATTGCGTTGATACATTGCAACGCAGCAAGGCGACACTGCCGGGTCCAACTAATTCTCTAACCGCAATGAGAAGGTGAAATATATCGAGGAACGGCATAGAGCCCTCAAACACACTCGTTGAGTCC'))
