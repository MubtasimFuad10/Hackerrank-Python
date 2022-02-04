from itertools import permutations
from math import perm
str, n=input().split()
permu=list(permutations(sorted(str), int(n)))

for i in range(len(permu)):
    print("".join(permu[i]))
