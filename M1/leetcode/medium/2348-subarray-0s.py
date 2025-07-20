# https://leetcode.com/problems/number-of-zero-filled-subarrays/


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        prev = 0
        for i in nums:
            if i == 0:
                total += prev + 1
                prev += 1
            else:
                prev = 0
        return total
