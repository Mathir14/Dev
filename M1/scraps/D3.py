# grade evaluator 
x = int(input("Enter marks: "))
if x >= 90:
    print('A')
elif 80 <= x <= 89:
    print('B')
elif 70 <= x <= 79:
    print('C')
elif 60 <= x <= 69:
    print('D')
else:
    print('F')

print('checkpoint')

# age group
age = int(input("Enter age: "))
if age < 13:
    print('Child')
elif 13 <= age <= 19:
    print('Teenager')
elif 20 <= age <= 59:
    print('Adult')
else:
    print('Senior')

print('checkpoint')

# odd even pos neg
num = int(input("Enter number: "))
if num == 0:
    print('Zero')
elif num % 2 == 0:
    if num > 0:
        print('Even and Positive')
    else:
        print('Even and Negative')
else:
    if num > 0:
        print('Odd and Positive')
    else:
        print('Odd and Negative')

print('checkpoint')

# simple calc
val = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
exp = input("Enter operation (+, -, *, /): ")

if exp == '+':
    print(val + val2)
elif exp == '-':
    print(val - val2)
elif exp == '*':
    print(val * val2)
elif exp == '/':
    if val2 == 0:
        print('Cannot divide by zero')
    else:
        print(val / val2)
else:
    print("Invalid operator")

print('checkpoint')

# login system
user = 'mathir'
passwrd = 'mathir14'

loginuser = input("Enter username: ")
loginpasswrd = input("Enter password: ")

if user == loginuser:
    if passwrd == loginpasswrd:
        print("Login successful")
    else:
        print('Incorrect password')
else:
    print('Invalid username')

print('checkpoint')

# short-circuit logic example
fd = '1'
fg = None
if fd == '1' and fg and fg > 0:
    print('something')

print('checkpoint')
