# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        res = []

        for curr in range(len(nums)):
            
            while q and (nums[q[-1]] < nums[curr]):
                q.pop()
            
            q.append(curr)

            if q[0] <= curr - k:
                q.popleft()
            
            if curr >= k - 1:
                res.append(nums[q[0]])

        return res