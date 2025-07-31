# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []

        hp = Counter(p)
        hs = Counter(s[: len(p)])

        if hp == hs:
            res.append(0)

        left = 0
        for right in range(len(p), len(s)):

            hs[s[left]] -= 1
            if hs[s[left]] == 0:
                del hs[s[left]]

            hs[s[right]] = hs.get(s[right], 0) + 1

            left += 1
            if hp == hs:
                res.append(left)

        return res
