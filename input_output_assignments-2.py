"""
Write a Python program that asks the user to enter their name using the input() function, and then prints a greeting message using the print() function. For example, if the user enters "Alice", the program should print "Hello, Alice!"
"""
s=input("Enter name :")
print("Hello,",s,'!',sep='')


"""
WAP to print the following output in single of code
'Hello' : dynamic using input()
'Anil' : dynamic using input()
Note: please use print() to combine the output
Final output format:
Hello Anil
Hi Anil
I Love Python
"""
s1=input("Enter hello:")
s2=input("Enter name:")
print(s1,s2)
s1=input("Enter hello:")
s2=input("Enter name:")
print(s1,s2)
s1=input("Enter i love:")
s2=input("Enter python:")
print(s1,s2)

"""
Write a script that asks the user for their name, age, and favorite color, and then prints a single sentence summarizing this information in a formatted string.
"""

s=input("Enter name:")
a=input("enter age :")
c=input("Enter fav color :")
print("its",s,"of age",a,"and his fav color is",c)
