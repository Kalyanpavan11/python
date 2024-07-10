# Assignment-1: if condition
# Check if a person is eligible to vote based on their age

# Input: Age of the person

# Check if the person is eligible to vote
age=int(input("enter the age :"))
if age >=18:
    print("eligible to vote")
else:
    print(" not eligible to vote")

# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative

num=int(input("enter the num :"))
if num>=0:
    print("positive num")
else:
    print("negative num")

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

num=int(input("enter the num :"))
if num%2:
    print("odd num")
else:
    print("even num")


# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers

a=int(input("enter the num :"))
b=int(input("enter the num :"))
c=int(input("enter the num :"))
if a>b:
    if a>c:
        print(a,"is the greatest")
    else :
        print(c,"is the greatest")
else:
    if b>c:
        print(b,"is the greatest")
    else :
        print(c,"is the greatest")

# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""

tp=10
age=int(input("enter the age :"))
time=int(input("enter the time :"))
zone=input("am/pm :")


if age<=12 or age>=65:
    tp=tp*0.5

if zone=='pm':
    time+=12
    
if time<17:
    tp=tp*0.75

print("The price :",tp)

# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population

a=int(input("enter the population of city a :"))
b=int(input("enter the population of city b :"))
c=int(input("enter the population of city c :"))
if a>b:
    if a>c:
        print(a,"is the greatest")
    else :
        print(c,"is the greatest")
else:
    if b>c:
        print(b,"is the greatest")
    else :
        print(c,"is the greatest")
