# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/

# prefix method


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = max_val = min_val = res = 0

        for num in nums:
            prefix += num

            res = max(res, abs(prefix - max_val), abs(prefix - min_val))

            max_val = max_val if max_val > prefix else prefix
            min_val = min_val if min_val < prefix else prefix

        return res


# kadane's method
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_val = curr_max = min_val = curr_min = 0

        for num in nums:
            curr_max = num if num > curr_max + num else curr_max + num
            max_val = max_val if max_val > curr_max else curr_max

            curr_min = num if num < curr_min + num else curr_min + num
            min_val = min_val if min_val < curr_min else curr_min

        return max(abs(max_val), abs(min_val))
