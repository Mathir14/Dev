Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

the problem requires us to find every subarray either [] [,] [,,]
whose sum equals k

to solve this efficiently,
instead of trying to find every combination,

we simply check if the complement, or the x,
where current value + x = k

for every value we encounter during the loop,
we use a running sum which sums every value seen so far,

we use count to get the x value which is current_value -k ,
if it is present, its added to count, otherwise 0,

we stored the current value in prefix using get()+1

we finally return the count

which is, the number of times x has been found

Time O(n)
Space O(n)
