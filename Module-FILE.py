
# ******************MyCode.py***************************************


print("Welcome to module Operations")
a=int(input("Enter no:"))
b=int(input("enter no.:"))

from Calc import *

print("1. for add")
print("2. for sub")
print("3. for mul")
print("4. for div")
n=int(input("Enter choice:"))

if n==1:
    print(add(a,b))
elif n==2:
    print(sub(a,b))
elif n==3:
    print(mul(a,b))
elif n==4:
    print(div(a,b))
else:
    print("Error")


# *************************Calc.py*****************************

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
