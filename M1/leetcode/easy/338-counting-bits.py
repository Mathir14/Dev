# https://leetcode.com/problems/counting-bits/description/


class Solution:
    def countBits(self, n: int) -> List[int]:
        value = [0] * (n + 1)
        for i in range(n + 1):
            value[i] = value[i >> 1] + (i & 1)
        return value
