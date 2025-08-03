# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):

            hmap = {}
            left = res = 0

            for right in range(len(nums)):

                hmap[nums[right]] = hmap.get(nums[right],0)+1

                if hmap[nums[right]] == 1:
                    k-=1

                while k < 0:
                    hmap[nums[left]] -=1

                    if hmap[nums[left]] == 0:
                        k+=1

                    left +=1

                res += right - left + 1
            return res

        return atmost(k) - atmost(k-1)