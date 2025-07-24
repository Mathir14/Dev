# https://leetcode.com/problems/maximum-number-of-balloons/description/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {}
        for i in text:
            if i in "balloon":
                hash[i] = hash.get(i, 0) + 1
        return min(
            hash.get("b", 0),
            hash.get("a", 0),
            hash.get("l", 0) // 2,
            hash.get("o", 0) // 2,
            hash.get("n", 0),
        )
