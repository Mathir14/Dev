# https://leetcode.com/problems/valid-anagram

#bruteforce

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for item in set(s): 
            if s.count(item) != t.count(item):
                return False
        return True

# counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

# manual implementation 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char,0)+ 1 
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True
