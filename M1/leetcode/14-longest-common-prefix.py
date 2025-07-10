# https://leetcode.com/problems/longest-common-prefix/

# initial solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        map = {}
        outp = ''
        for i, val in enumerate(strs[0]):
            map[i] = val
        count = 0
        while count < len(strs[0]):
            for i in strs[1:]:
                if count >= len(i) or i[count] != map[count]:
                    return outp
            outp = outp + map[count]
            count +=1
        return outp

# optimal solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        outp = ''
        for count in range (len(strs[0])):
            char = strs[0][count]
            for i in strs[1:]:
                if count >= len(i) or i[count] != char:
                    return outp
            outp += char
        return outp