# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        count = prefix = 0
        res = {0: 1}

        for num in arr:
            prefix += num
            odd_even = prefix % 2

            opposite = 1 - odd_even

            count += res.get(opposite, 0)
            res[odd_even] = res.get(odd_even, 0) + 1

        return count % mod
