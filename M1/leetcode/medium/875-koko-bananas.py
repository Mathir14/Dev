# https://leetcode.com/problems/koko-eating-bananas/description/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid  # fast ceil
                if hours > h:
                    break
            if hours > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
