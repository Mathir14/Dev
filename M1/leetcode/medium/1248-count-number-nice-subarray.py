# https://leetcode.com/problems/count-number-of-nice-subarrays/description/


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            left = res = 0
            for right in range(len(nums)):

                if nums[right] & 1:
                    k -= 1

                while k < 0:
                    if nums[left] & 1:
                        k += 1
                    left += 1

                res += right - left + 1
            return res

        return atmost(k) - atmost(k - 1)
