# https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = prefix = 0
        prefix_map = {0: 1}

        for num in nums:

            prefix += num

            count += prefix_map.get(prefix - goal, 0)
            prefix_map[prefix] = prefix_map.get(prefix, 0) + 1

        return count
