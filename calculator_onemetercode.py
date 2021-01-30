# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while True:
    print('"WELCOME TO MY SIMPLE CALCULATOR IN PYTHON"')
    fnum = int(input('Type your first number:'))
    snum = int(input('Type your second number'))
    print('[1]Multiply, [2]Divide, [3]Add, [4]Subtract,')
    choices = int(input('Type your choice:'))
    if choices == 1:
        print('The product of',fnum,'and',snum,'is',multiply(fnum,snum))
    elif choices == 2:
        print('The QUOTIENT of', fnum, 'and', snum, 'is', divide(fnum,snum))
    elif choices == 3:
        print('The SUM of', fnum, 'and', snum, 'is', add(fnum,snum))
    elif choices == 4:
        print('The DIFFERENCE of', fnum, 'and', snum, 'is', subtract(fnum,snum))
    else:
        print('You have imputed a wrong number')
        break
    question = input('Do you want to input again?Y/N:')
    if question == 'Y' or question == 'y': pass
    else:
        print('Thank you for using my simple calculator')
        break
