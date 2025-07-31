# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hsh1 = {}
        for i in s1:
            hsh1[i] = hsh1.get(i,0) + 1
    
        hsh2 = {}
        for i in s2[:len(s1)]:
            hsh2[i] = hsh2.get(i,0)+1

        if hsh1 == hsh2:
            return True

        left = 0
        for right in range(len(s1),len(s2)):

            hsh2[s2[right]] = hsh2.get(s2[right],0)+1

            hsh2[s2[left]] -=1
            if hsh2[s2[left]] == 0:
                del hsh2[s2[left]]

            if hsh1 == hsh2:
                return True
            left+=1

        return False
        
