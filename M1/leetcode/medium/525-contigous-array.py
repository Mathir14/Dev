# https://leetcode.com/problems/contiguous-array/description/


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        balance = 0
        max_len = 0

        for index, value in enumerate(nums):
            balance += 1 if value == 1 else -1
            if balance in seen:
                max_len = (
                    max_len
                    if max_len > (index - seen[balance])
                    else (index - seen[balance])
                )
            else:
                seen[balance] = index

        return max_len
