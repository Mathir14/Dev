# https://leetcode.com/problems/number-of-good-pairs/description/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        res = 0
        for i in nums:
            res += hash.get(i, 0)
            hash[i] = hash.get(i, 0) + 1
        return res
