"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
a=75
B=3.14
print(a,B)
print(type(a),type(B))


'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
x=1+2j
y=1+2J
print(x,type(x))
print(y,type(y))


'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
import sys
a=123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
print(a,sys.getsizeof(a),type(a))
