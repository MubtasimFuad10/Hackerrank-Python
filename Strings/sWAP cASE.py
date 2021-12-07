def swap_case(s):
    res = ''
    for word in s:
        if word.islower():
            res += word.upper()
        else:
            res += word.lower()
    return res

if __name__ == '__main__':
    s=input()
    print(swap_case(s))