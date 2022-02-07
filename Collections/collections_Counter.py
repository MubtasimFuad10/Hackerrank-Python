from collections import Counter
x=int(input())
mylist=[]

for i in range(0,x):
    shoe_size = int(input())
    mylist.append(shoe_size)

n=int(input())
amount=0
for i in range(n):
    size, price = map(int, int(input().split()))
    if shoe_size[size]==True:
        amount+=price
        shoe_size[size]-=1
    print(amount)

