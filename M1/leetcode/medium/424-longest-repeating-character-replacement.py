# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = right = 0
        hash_map = {}

        maxf = 0
        res = 0

        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            maxf = maxf if maxf > hash_map[s[right]] else hash_map[s[right]]

            while ((right - left + 1) - maxf) > k:
                hash_map[s[left]] -= 1
                left += 1

            res = res if res > right - left + 1 else right - left + 1

        return res
