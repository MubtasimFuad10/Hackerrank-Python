if __name__ == '__main__':
    n=int(input())
    integer_list=map(int,input().strip().split())
    t = tuple(integer_list)
    print(hash(t)) #hash() is a function in python that give us a hash value of a object
