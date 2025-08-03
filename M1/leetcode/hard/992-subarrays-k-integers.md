Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

learned that instead of counting exactly k, it's easier to just count at most k and subtract at most k-1 to get exactly k

reused the sliding window trick: push right, shrink from left only when you go over the limit

used a frequency map to track how many of each element are in the window

idea: every time you add a new element to the window, if it’s the first time seeing it, you’re using up one of your k distinct slots

if you run out (k < 0), start shrinking from the left until you're valid again

each time the window is valid, you add right - left + 1 to the answer, because every subarray ending at right and starting anywhere from left to right is valid

finally, just call this whole thing twice: once for k, once for k-1, subtract to get the count of subarrays with exactly k distinct

what i learned:

tracking k like a budget instead of trying to match it

counting valid subarrays by length of window

filtering good answers out of larger pool is easier than trying to nail them directly

map-based sliding window is powerful af
