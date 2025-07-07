# odd or even 
print("even" if int(input()) % 2 == 0 else "odd")

print("checkpoint")

# calc
print(int(input()) + int(input()))

print("checkpoint")

#max of 3
a,b,c = [int(input()) for i in range(3)]
print(max(a,b,c))

print("checkpoint")

#list sum
ls = [x for x in range(int(input())+1)]
tot = 0
for i in ls:
    tot += i
print(tot)
print("checkpoint")

#reverse string
rev = input()
print(rev[::-1])

print("checkpoint")

#fact
n = int(input())
fact = 1
while n>1:
    fact *=n
    n-=1
print(fact)

print("checkpoint")

#vowels
vow = input()
count = 0
for i in vow:
    if i.lower() in 'aeiou':
        count += 1
print(count)

print('checkpoint')

#fizzbuzz
for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')

print('checkpoint')

#palindrome
pali = input()
if pali == pali[::-1]:
    print('palindrome')

print('checkpoint')

#dic
dic = {}
for i in range(3):
    x = input()
    y = input()
    dic[x] = y
print(dic)

print('checkpoint')