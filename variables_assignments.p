"""
Assignment-1:
WAP to assign 3 values (string, int, float)
to 3 variables (Student_name, Roll_Number, Percentage_of_marks).
print the values using print function.
"""

Student_name=input("enter student name :")
Roll_Number=int(input("enter per of marks :"))
Percentage_of_marks=float(input("enter per:"))
print(Student_name,Roll_Number,Percentage_of_marks)

"""
Assignment-2:
WAP to assign value 6 to two different variables (example: a1, b1) 
using single line of code.
Check the variable values and memory address.
"""
a1,b1=6,6
print("a1=",a1,id(a1),"b1=",b1,id(b1))

"""
Assignment-3:
WAP to assign multiple values to multiple variables
in single line of code
After assigning, print and check the values
"""'
a,b,c,d=1,2,3,4
print(a,b,c,d)
