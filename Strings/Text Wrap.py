from textwrap import TextWrapper
from textwrap import dedent
import textwrap

def wrap(string, max_width):
  
    wrapper =TextWrapper(width=max_width)
    de_text = dedent(text=string)
    result = wrapper.fill(text=de_text)
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)