# https://leetcode.com/problems/subarray-sum-equals-k/description/


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current = 0
        prefix = {0: 1}

        for num in nums:
            current += num
            count += prefix.get(current - k, 0)
            prefix[current] = prefix.get(current, 0) + 1
        return count
