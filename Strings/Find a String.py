def count_substring(string, sub_string):
    cn=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string): #here startswith() returns true if the string starts with the specified value, otherwise false.
           cn=cn+1
    return cn

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)