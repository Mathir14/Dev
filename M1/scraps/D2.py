# compare 2
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

print('checkpoint')

#divisible by 3 and 5

n = int(input())
if n % 3 == 0:
    print("yep")
else:
    print('false')

print('checkpoint')

# swap

x = 100
y = 101
print(x,y)
x = x ^ y
y = x ^ y
x = x ^ y
print(x,y)

print('checkpoint')

# power of 2

s = 10
d = 2
fl = False
while d <= s:
    if s == d:
        fl = True
        break
    d = d << 1
print(fl)

print('checkpoint')

# count 1s

b = 10
bn = (bin(b))
print(bn.count('1'))

print('checkpoint')