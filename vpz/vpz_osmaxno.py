import sys


# limit values of the integers does not exist
a = sys.maxsize
# a is 9223372036854775807
print(a)

b = 255
c = 1000

a1 = a * c
# a1 is 9223372036854775807000
print(a1)
a2 = (a1 + c) / b
# a2 is 36170086419038336501
print(a2)