# https://leetcode.com/problems/max-consecutive-ones-iii/

# just as good


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero = 0
        length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            length = (right - left + 1) if (right - left + 1) > length else length
        return length


# math hack


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i + 1
