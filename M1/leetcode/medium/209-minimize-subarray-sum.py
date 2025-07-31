# https://leetcode.com/problems/minimum-size-subarray-sum/description/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = inf

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = (
                    min_len if min_len < (right - left + 1) else (right - left + 1)
                )
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == inf else min_len
