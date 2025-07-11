# sum of n

n = int(input())
sum = 0
for i in range(n+1):
    sum += i
print(sum)

# other method
print(n*(n+1)//2)

print('checkpoint')

# fact

val = int(input())
ft = 1
for i in range(1,val+1):
    ft *= i
print(ft)

print('checkpoint')

# prime

import math
pr = int(input())
res = True
vl = int(math.sqrt(pr))
for i in range(1,vl+1):
    if pr < 2:
        res = False
        break
    if i == 1 or i == pr:
        continue
    if pr % i == 0:
        res = False
        break
print(res)

print('checkpoint')

#fib

f1 = 0
f2 = 1
temp = 0
terms = int(input())
print(f1)
print(f2)
while terms > 2:
    temp = f1 + f2
    print(temp)
    f1 = f2
    f2 = temp
    terms -=1

print('checkpoint')

# even
for i in range(1,101):
    if i == 50:
        continue
    if i % 2 == 0:
        print(i)

print('checkpoint')

# 5 n 7
low = int(input())
high = int(input())
for i in range(low,high+1):
    if i %  7 == 0 and i % 5 == 0:
        print(i)
        break

print('checkpoint')

# else block

arr = [x for x in range(11)]
for i in arr:
    if i == 11:
        break
else:
    print('not found')

print('checkpoint')
