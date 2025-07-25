# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev = 0
        
        for char in reversed(s):
            curr = value[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
                prev = curr
        return total