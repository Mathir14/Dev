# sum all with *args
def sum(*args):
    res = 0
    for i in args:
        res+=i
    return res
print(sum(1,2,3,4,5,6,7,8,9,10))

print('checkpoint')

# kwargs

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
info(name = 'MV', age = 19, gender = 'M')

print('checkpoint')

# combinations

def func(a,b,*args,**kwargs):
    print(a)
    print(b)
    for x in args:
        print(x)
    for key, value in kwargs.items():
        print(key, value)
func(10,20,30,40,50,x='a',y='b')

print('checkpoint')