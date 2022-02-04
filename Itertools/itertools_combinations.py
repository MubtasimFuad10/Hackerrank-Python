# from itertools import combinations
# str, n=input().split()
# strings=sorted(str)
# for i in range(len(strings)):
#     print(strings[i], end="\n")
# combi=list(combinations(sorted(str),int(n)))

# for i in range(len(combi)):
#     print("".join(combi[i]))

from itertools import combinations
str, n = input().split()
for i in range(1,int(n)+1):
    combi=list(combinations(sorted(str),i))
    for i in combi:
      print("".join(i))