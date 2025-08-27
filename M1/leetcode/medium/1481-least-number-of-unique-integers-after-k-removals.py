# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        while k:
            if counts[-1] > k:
                break
            k -= counts[-1]
            counts.pop()
        return len(counts)
