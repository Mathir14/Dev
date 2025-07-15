# local

def greet():
    name = "Alice"
    print(name)

greet()

# global 

name = "Bob"

def greet():
    global name # to modify the global var inside a func
    print(name)

greet()
print(name)

# non local

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("inner:", x)
    inner()
    print("outer:", x)

outer()

# zip

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zips multiple values in an iterable into pairs/ tuples

# all

# returns True if all element in an iterable is True

marks = [80, 75, 90]
print(all(m > 50 for m in marks))  # True
print(all([True, False, True]))    # False

# any

# returns True if atleast one element in an iterable is True

marks = [30, 45, 60]
print(any(m >= 50 for m in marks))  # True
print(any([False, False, False]))   # False

# sorted

nums = [4, 2, 9, 1]
print(sorted(nums))        # [1, 2, 4, 9]
print(sorted(nums, reverse=True))  # [9, 4, 2, 1]

# can use key for custom sorting