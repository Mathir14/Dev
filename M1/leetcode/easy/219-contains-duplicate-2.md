Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

this problem is about finding a duplicate within a sliding window,
so we are given an array of integers, and k
k is the distance covered by the sliding window.

so basically, we check if any value within that window is duplicate,
such that the index of the two values i and j,
their difference absolute should be lesser than or equal to k,

so we use hash,
we iterate through the array,
on first appearance, we add it to the hash, the element as the key and it's index
as the value,

if an element appears again, which means it is in the hash already, we check if it's i j difference absolute is <= k
if it is, we return True

if it iterates through the whole array which means it completed without returning True,
we return False

time O(n)
space O(n)
