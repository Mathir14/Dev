# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = " ".join(s[::-1])
        return ans


# we are given a string with words seperated by any n number of whitespaces
# required to return a string, where the words are reversed, but with only 1 tailing whitespace

# example, consider this string ' Hello world   I am idk'
# return 'idk am I world Hello'

# we use .split() to remove the whitespaces and just store the words in a list,
# used ''.join to join every word in the list from reverse ::-1
