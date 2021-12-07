if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split())) #set is used for unique values. map is used for mapping.
    print(sorted(arr)[-2]) #so , sorted in ascending order. so [-2] is used for getting the index in reverse way.

   
