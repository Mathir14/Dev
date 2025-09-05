Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

usual solution:

first, split the string s into a list of words

if the number of words doesn’t match the length of the pattern, return false immediately

create an empty dictionary to map pattern characters to words, and a set to keep track of words that are already used

iterate over each character in the pattern and its corresponding word:

if the character is already in the mapping and the mapped word is different from the current word, return false

if the character is not in the mapping but the word is already used by another character, return false

otherwise, add the character-to-word mapping and mark the word as used

after checking all pairs, return true

trick solution:

split s into words

check all in one line:

lengths of pattern and words match

number of unique chars equals number of unique words

number of unique char-word pairs equals both

return result of this check