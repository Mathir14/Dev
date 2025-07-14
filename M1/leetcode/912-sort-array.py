# https://leetcode.com/problems/sort-an-array/description/

# quick sort 

import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 0:
            return nums
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        center = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.sortArray(left) + center + self.sortArray(right)
    
# merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

