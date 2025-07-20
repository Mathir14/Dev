a simple string problem where we have to check if a word is valid, based on the given constraints:

A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

we need to check if the word satisfies the 4 given conditions,
used .isalnum() to check if all the characters in the word belong to alphabets and numbers
and len(word) to check if it had atleast 3 characters, if it failed either of these conditions, then it is not a valid word 
and we return False,
this is to filter out invalid words early since they have to have atleast 3 characters and belong to alpha numeric case

if it passed that condition, then the other two conditions have to be satisfied,
vowels and consonants, to store vowels we used set('aeiou') for faster lookups
to check the if the word has vowels and consonants,
we use word.lower() in for loop to check each character, we convert it to a set for faster lookup
we check if the character isalpha() which means it is an alphabet, if it is, we check if it exists in the set vowel, if it does, then count_vowel or cv becomes True, we do not need the exact count as they ask for atleast 1 meaning anything after that is not necessary,
and we have another condition, if character not in vowel, meaning it is an alphabet but not a vowel which means it is a consonant, then we set count_consonant or cc = True
we each if both cc and cv is true at every iteration for early break as all the conditions are by then, satisfied,
we return cc and cv, which is an and condition, it returns True if cc and cv passes the and condition, otherwise returns False