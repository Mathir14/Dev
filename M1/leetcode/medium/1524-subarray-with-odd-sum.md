Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16

so the problem requires us to return the number of subarrays whos sum is odd,

there's a trick to this,
if current prefix is odd, we need to check how many even subarrays are there,
and vice versa for even,

this way, lets say current prefix is odd, and there are 5 even subarrays before this,
that is 5 odd subarrays when u add the current prefix,

and vice versa for even,

this way, we can just get the number of evens or odds there are, opposite to current prefix
so that it becomes odd, because odd even is odd, even odd is odd, that's why
we try to get the count of the opposite subarrays

and we return the final count
