# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        for i in matrix:
            for j in i: 
                heapq.heappush(min_heap,j)
        
        for _ in range(k):
            res = heapq.heappop(min_heap)
        
        return res