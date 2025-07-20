# https://leetcode.com/problems/first-missing-positive/description/


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[i] != nums[x - 1]:
                nums[x - 1], nums[i] = nums[i], nums[x - 1]
            else:
                i += 1

        i = 0
        while i < n:
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return n + 1
