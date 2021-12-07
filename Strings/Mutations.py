
def mutate_string(string, position, character):
    return string[:position]+character+ string[position+1:]

if __name__ == '__main__':
    s = input()
    i,c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#NOTE:
"""what is 1: ?
    For Example:
    It is a notation that is used to get a slice of a list
    s = "You are learning Python"
    print(s[:]) # outputs "You are learning Python"
    print(s[1:6]) # outputs "ou ar", because s[1] is "o", s[5] is "r"
    print(s[10:]) # outputs "arning Python" because it's the slice from index 10 to the end of the string
    print(s[:10]) # outputs "You are le" because it's the slice from the start to index 9
"""
