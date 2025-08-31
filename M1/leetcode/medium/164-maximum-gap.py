# https://leetcode.com/problems/maximum-gap/description/


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        gap = 0
        nums.sort()
        right = 1
        while right < len(nums):
            gap = (
                gap
                if gap > (nums[right] - nums[right - 1])
                else (nums[right] - nums[right - 1])
            )
            right += 1
        return gap
