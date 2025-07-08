when comparing two strings, if the frequencies of the characters are the same, it is an anagram
ex : hello elhlo

note : regardless of how it sounds, 
"if there are same number of characters appearing same number of times, it is an anagram"


common edgecase:
if len(string_1) != len(string_2):
    return false

reason:
"if there are same number of characters appearing same number of times, it is an anagram"
which means it must be same in length,
by checking for the length of the strings, we can immediately rule them out as not anagrams if their length does not match

bruteforce method:
given two strings s and t,
we convert the string either s or t into a set in the for loop,
the purpose is to remove the duplicate characters so only unique characters remain,
and inside the body, we get the count of each character from the set
we do this for both the strings and if they are not equal then they are not anagrams, if they are equal down to the last character,
then they are anagrams,

an ex:
s = hello
t = elhlo
set(s) = helo (duplicates removed)
now we get the count of each character from both strings,
iter 1 : count(h) for both s and t : 1 and 1 so equal
iter 2 : count(e) for both s and t : 1 and 1 so equal
iter 3 : count(l) for both s and t : 2 and 2 so equal
iter 4 : count(o) for both s and t : 1 and 1 so equal

it has passed the entire loop meaning, regardless of how jumbled it is, if the characters and their count of appearances match, it is as anagram

the reason it's not preferred is because at every iteration, for every character, it goes through the entire string to get its count,
as s.count(item) == t.count(item), this line, takes every character from the set, and iterates through both the strings to get its count, now this has to repeat for every character, through the entire string for both s and t, while bruteforce may work for smaller sized strings, it is not scalable and is actually more resource intensive compared to its alternatives.

Counter function and Manual Method
Counter is a function inside the library collections, which is part of the standard library,
Counter(x) is used to count the frequency of elements in an iterable(be it list tuple or dict)
Counter is the C implementation of the manual method in python under the hood.

In manual method, we have an empty dict count = {}
for char in s:
    count[char] = count.get(char,0)+ 1 

this block of code does:
it uses the char as the key and uses get(),
.get(char,0)+1 works by, if char is present in the dict count, then it appends the char again into the dict and the count value is increased by 1 hence the + 1 outside get()
if the char is not present in the dict, then it appends the char into the dict and the 0 is increased by 1 meaning theres 1 of that char in the dict

for char in t:
    if char not in count or count[char] == 0:
        return False
        count[char] -= 1

this block of code does:
we now have the count of each characters in string s, now we iterate through the string t,
we check if the char is not present in dict count,
then that means the char from string t is not present in string s which means it is not an anagram

the second condition counter[char] == 0
is used to check if the count of the char is same for both strings,
after each iteration, the count of char is decreased by 1,
meaning if a char from string t is present more number of times than it is present in string s,
then at a certain number of iteration, the count of char in string s would be reduced to 0, yet it is present in string t, breaking the condition of same frequency meaning it is not an anagram.
