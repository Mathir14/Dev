# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() or word.lower() or word.title()


# detect capital — just check if word is all uppercase, all lowercase, or title case
# used built-in checks like `.upper() == word`, `.lower() == word`, or `.istitle()`

# manual check would be slower and messier
# one-liner using logical or chaining works fine here
