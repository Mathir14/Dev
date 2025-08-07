# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = prefix = 0

        prefix_map = {0: 1}
        for num in nums:

            prefix += num

            mod = (prefix % k + k) % k

            count += prefix_map.get(mod, 0)
            prefix_map[mod] = prefix_map.get(mod, 0) + 1

        return count
