# lamba

l1 = lambda x : x*x
print(l1(int(input())))

l2 = lambda x : True if x % 2 == 0 else False
print(l2(int(input())))

l3 = lambda x : x[-1]
print(l3(input()))

l4 = lambda x : x[::-1]
print(l4(input()))

print('checkpoint')

# map

names = ["mathir", "demon", "aqua"]
print(list(map(lambda x : x.upper(),names)))

print('checkpoint')

# filter

nums = [10, 15, 20, 30, 33, 60]
print(list(filter(lambda x : x % 5 == 0 and x % 3 == 0,nums)))

print('checkpoint')

# reduce

from functools import reduce

print(reduce(lambda x , y : x * y, nums))
words = ["you", "are", "freaking", "amazing"]
print(reduce(lambda x , y : x if len(x) > len(y) else y ,words))

print('checkpoint')

# closure

def power(x):
    def val(y):
        return x ** y
    return val
raiseto = power(2)
print(raiseto(10))

def tag(x):
    def content(y):
        return f"<{x}>{y}</{x}>"
    return content
t = tag('h1')
print(t('Hello'))

print('checkpoint')

# func as arg

def apply_twice(func,val):
    return func(func(val))
def double(x): return x * 2
print(apply_twice(double, 3))  # 12

print('checkpoint')

# decorators

from functools import wraps

def status(func):
    @wraps(func)
    def wrap():
        print('[Running]')
        func()
        print('[Done]')
    return wrap

@status
def greet():
    print('Heyyy')

greet()
print(greet.__name__)


def debug(func):
    def logger(*args,**kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        res = func(*args,**kwargs)
        print(f"returned {res}")
        return res
    return logger

@debug
def add(*args, **kwargs):
    extra = sum(kwargs.values())
    return(sum(args) + extra)

add(1,2,3,4,5, kwarg = 10, kwarg1 = 20)

import time

def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[{func.__name__}] failed on attempt {attempt}: {e}")
            print(f"[{func.__name__}] all {n} attempts failed.")
        return wrapper
    return decorator

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


def repeat(n):
    def deco(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrap
    return deco
            

def status(func):
    @wraps(func)
    def wrap():
        print('[Running]')
        func()
        print('[Done]')
    return wrap
@timer
@status
@retry(2)
@repeat(2)
def greet():
    print('Heyyy')

greet()

