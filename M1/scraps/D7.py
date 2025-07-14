# tuple

def tup(x):
    return min(x),max(x)
print(tup((1,2,3,4,5,6,7,8,9)))

a = 10
b = 20
a,b = b,a

pair = [(1,2),(3,4),(5,6),(7,8),(9,10)]
first = []
second = []
for i in pair:
    first.append(i[0])
    second.append(i[1])

print(first)
print(second)

def anyval(*args):
    return tuple(args)
print(anyval(1,2,3,4,5,6,7,8,9))

a,_,c = (1,2,3)
print(a,c)

def counter(tup,x):
    return tup.count(x)
print(counter((1,2,3,4,5,5,6,7,8,9),5))

print('checkpoint')

# sets

lis = [1,2,3,3,4,5,6,7,7,8,8]
print(set(lis))

a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a | b)
print(a & b)
print(a-b)

c = set('hello')
d = set('goodbye')
print(c & d)

print(a.issubset(b))

def uniq(x):
    return len(x) == len(set(x))
print(uniq([1,2,3,4,5,6]))

print('checkpoint')

# dicts

dic = {
    'name' : 'Mathir',
    'age' : 18,
    'country' : 'India'
}

for i in dic.values():
    print(i)

dic['profession'] = 'student'
dic['age'] = 19

print(dic.pop('country'))

dic.get('key',0)

dic2 = {}
stri = 'hello'
for i in stri:
    dic2[i] = dic2.get(i,0)+1
for i,j in dic2.items():
    print(i,j)

sqr = {x: x**2 for x in range(6)}

lis2 = ['hi', 'hello', 'bye']
dic3 = {}
for i in lis2:
    dic3[i] = len(i)

dic3 = {}
stri = 'hwllo'
for i in stri:
    dic3[i] = dic3.get(i,0)+1
print(dic3.items())

students = {
    'stud1' : {
        'name' : 'abc',
        'age' : 19,
        'grades' : [80,90,70,90]
    },
    'stud2' : {
        'name' : 'ded',
        'age' : 19,
        'grades' : [80,90,70,90]
    },
    'stud3' : {
        'name' : 'ghi',
        'age' : 19,
        'grades' : [80,90,70,90]
    }
}
for i in students.keys():
    avg = sum(students[i]['grades'])/len(students[i]['grades'])
    print(students[i]['name'], sum(students[i]['grades'])/len(students[i]['grades']))
    students[i]['status'] = "Pass" if avg >= 50 else "Fail"
