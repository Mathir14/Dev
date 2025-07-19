# name

name = [input() for x in range(5)]

with open('name.txt','a') as f:
    for x in name:
        f.write(x+'\n')

with open('name.txt','r') as f:
    for x in f:
        print(x.strip())

# error log

def error_log(message):
    with open('error_log.txt','a') as f:
        f.write('Log - '+ message + '\n')

error_log('Testing 1')
error_log('Testing 2')
error_log('Testing 3')

with open('error_log.txt','r') as f:
    for line in f:
        print(line.strip())

# word count

count = 0
with open('error_log.txt','r') as f:
    for line in f:
        count += len(line.split())
print(count)

# copy one file to another file

f = open('error_log.txt','r')
s = open('destination.txt','w')
for line in f:
    s.write(line)
f.close()
s.close()

# reverse

f = open('error_log.txt','r')
s = open('destination.txt','w')
content = f.readlines()
for x in reversed(content):
    s.write(x)
f.close()
s.close()

# numbers

f = open('data.txt','a+')
for x in range(1,11):
    f.write(str(x) + '\n')
f.close()
f = open('data.txt','r')
e = open('even.txt','a')
o = open('odd.txt','a')
for line in f:
    x = int(line.strip())
    if x % 2 == 0:
        e.write(str(x) + '\n')
    else:
        o.write(str(x) + '\n')
f.close()
e.close()
o.close()