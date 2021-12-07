
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i+j+k) != n])

    #List Comprehension: 
     #[expre -- for loop- if] <-- the basic structure of list comprehension. here, first one is expression,
        #2nd is for loop for adding and third if condition if there any.

