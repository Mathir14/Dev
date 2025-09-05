# https://leetcode.com/problems/word-pattern/description/

# usual 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        mapping = {}
        used = set()

        for char,word in zip(pattern,words):
            if char in mapping:
                if mapping[char] != word:
                    return False
            
            else:
                if word in used:
                    return False
                mapping[char] = word
                used.add(word)
        return True

# trick

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return( len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern,words))))