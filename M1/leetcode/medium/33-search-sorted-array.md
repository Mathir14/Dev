here is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

array is rotated but still sorted in two halves.
binary search with extra logic to decide which half to move.
check if mid is answer. if not:

if left half is sorted (nums[low] ≤ nums[mid]):
check if target lies in that half, adjust high, else move low.

else right half is sorted:
check if target lies in that half, adjust low, else move high.
keeps halving until found or empty.

dry run
nums=[4,5,6,7,0,1,2], target=0

low=0, high=6
mid=3 → nums[3]=7 ≠ 0
left half sorted (4..7). target=0 not in [4..7] → low=4
low=4, high=6
mid=5 → nums[5]=1 ≠ 0
right half sorted (1..2). target=0 not in [1..2] → high=4
low=4, high=4
mid=4 → nums[4]=0 → found → return 4

ans=4
