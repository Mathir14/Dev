# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        count = {}

        for char in magazine:
            count[char] = count.get(char, 0) + 1

        for char in ransomNote:
            if count.get(char, 0) == 0:
                return False
            count[char] -= 1

        return True
