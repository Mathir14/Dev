# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        if not needle:
            return 0
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1