def add(a,b):
    result = a+b
    print(result)

def sub(a,b):
    result = a-b
    print(result)

def mul(a,b):
    result = a*b
    print(result)

def div(a,b):
    result = a/b
    print(result)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation =input("Enter the operation: ")

if operation == "+":
    add(a,b)
elif operation == "-":
    sub(a,b)
elif operation == "*":
    mul(a,b)
elif operation == "/":
    div(a,b)
else:
    print("Invalid input!")
