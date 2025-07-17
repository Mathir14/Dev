# basic exception handling

try:
    x = int(input())
    y = int(input())
    z = x / y

except ZeroDivisionError:
    print(ZeroDivisionError, "Division By Zero")

else:
    print(z)

finally:
    print('Operation complete')