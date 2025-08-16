# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            current = 0
            days_taken = 1

            for weight in weights:
                if current + weight > mid:
                    days_taken += 1
                    current = 0
                current += weight

            if days_taken > days:
                low = mid + 1
            else:
                high = mid

        return low
