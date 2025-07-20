# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0   
        if s == '':
            return True           
        while right < len(t):         
            if s[left] == t[right]:
                left+=1           
                if left == len(s):
                    return True
            right+=1               
        return False