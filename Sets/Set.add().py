n = int(input())
sets = set()
for i in range(n):
    sets.add(input()) #adding string to the set
print(len(sets))  # here, len its because we need number of times its printing the stamps
                    #and as usual sets are unique. So, there will be no same values/numbers in sets.