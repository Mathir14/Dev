# https://leetcode.com/problems/largest-number/submissions/

# cmp_to_key

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            a, b = str(a), str(b)
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(compare))
        result = "".join(map(str, nums))
        return "0" if result[0] == "0" else result


# shortcut


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = "".join(sorted(list(map(str, nums)), key=lambda x: x * 10, reverse=True))
        return "0" if nums[0] == "0" else nums
