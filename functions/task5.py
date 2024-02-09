from itertools import permutations

def allperm(str):
    perm = permutations(str)
    for i in list(perm):
        return i