# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        left = 0
        length = 0

        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            length = length if length > right - left + 1 else right - left + 1
        return length
