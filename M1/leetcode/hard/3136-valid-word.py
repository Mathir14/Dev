# https://leetcode.com/problems/valid-word/description/

class Solution:
    def isValid(self, word: str) -> bool:
        vowel = set('aeiou')
        cv = False
        cc = False
        if not word.isalnum() or len(word) < 3:
            return False
        for i in set(word.lower()):
            if i.isalpha():
                if i in vowel:
                    cv = True
                else:
                    cc = True
            if cc and cv :
                break
        return cc and cv