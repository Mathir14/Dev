# https://leetcode.com/problems/continuous-subarray-sum/description/


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        prefix_map = {0: -1}

        for index in range(len(nums)):
            prefix += nums[index]
            mod = prefix % k if prefix >= k else prefix

            if mod in prefix_map:
                if index - prefix_map[mod] > 1:
                    return True
            else:
                prefix_map[mod] = index

        return False
