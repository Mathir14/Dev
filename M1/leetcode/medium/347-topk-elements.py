# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        heap = [(-value, key) for key, value in hash.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
