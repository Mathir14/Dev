# string operations
string = 'HIHIHIHIHIHIHI'
print(string[:6])
print(string[::-1])

name = 'john'
age = 19
print("My name is {} and I am {} years old".format("John", 25))
print(f"My name is {name} and I am {age}")

print(' Hello   '.strip())
print("TEST".lower())
print("test".upper())
print("word word".replace("word", "letter"))
print("hello world".split())
print("hello world".startswith('h'))
print('abc123'.isalnum())

# exercises

print('hello i love her'.upper())
print('word love'.replace('word','love'))
print(string.count('I'))
string = ' HihiHihihi   '
print(True if string.lower().strip() == string.lower().strip()[::-1] else False)