Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n \* k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 \* 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

store earliest index of each prefix mod in prefix_map
if current prefix mod seen before, check if subarray length (current_index - earliest_index) > 1

if yes return True
else keep storing first occurrence of each mod

start prefix_map with {0: -1} to handle subarrays from start

example nums = [0,2], k=2:

i=0 prefix=0 mod=0 in map at -1, length 1 not >1 continue
i=1 prefix=2 mod=0 in map at -1, length 2 >1 return True

correctly detects subarray [0,2] sum divisible by k length >= 2
this runs in O(n) time and O(k) space
