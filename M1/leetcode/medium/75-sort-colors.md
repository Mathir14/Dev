Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

use three pointers

low → boundary for next 0

mid → current element

high → boundary for next 2

if 0 → swap with low, move both

if 1 → just move mid

if 2 → swap with high, move high only (don’t move mid yet)

time → O(n)
space → O(1)
