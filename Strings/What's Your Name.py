#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first_name} {last_name}! You just delved into python.")
    #print("Hello {} {}! You just delved into python.".format(first_name,last_name)) #or we can write on this way too.
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)