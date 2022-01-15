import itertools


A=list(map(int, input().split()))
B=list(map(int, input().split()))

print(*itertools.product(A, B)) #  * operator is an unpacking operator that will unpack the values from any iterable object.