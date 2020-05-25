def permutations(string):
    #using itertools
    import itertools as it
    permutations = []
    j = ''
    for i in sorted(it.permutations(string, len(string))):
        if j != i:
            permutations.append(''.join(i))
        j=i
    return permutations
