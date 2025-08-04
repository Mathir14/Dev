# https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/

from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:

        freq = Counter(s)

        n = len(s)
        target = n // 4
        res = n

        left = 0
        for right in range(n):
            freq[s[right]] -= 1

            while left < n and all(freq[c] <= target for c in "QWER"):
                res = res if res < (right - left + 1) else (right - left + 1)
                freq[s[left]] += 1
                left += 1

        return res
