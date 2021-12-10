n=int(input())
sets= set(map(int, input().split()))
m = int(input())
for i in range(m):
    eval('sets.{0}({1})'.format(*input().split()+[' '])) #here eval parses the string expression and detect and runs the code

print(sum(sets))


# for example of eval() --> 

#     num =10
#     square_number = eval(num * num)
#     print(num) // output: 100


