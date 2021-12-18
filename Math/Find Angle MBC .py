import math
a, b = int(input()), int(input())
c=int(round(math.degrees(math.atan2(a, b)))) #--> returns the arc tangent of y/x, in radians
print(c, end=u'\N{DEGREE SIGN}') #--> '\N{DEGREE SIGN}' this is used to print degree sign.




#source:
#  https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python

#  https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals