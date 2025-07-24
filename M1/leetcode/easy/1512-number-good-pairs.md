Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

the problem is about finding the maximum number of combinations a value can be paired with its duplicates,
a tiny constraint is index of i must be lower than j, which is fine for almost all cases,

this problem follows the prev + 1 method for counting number of 0 sub array combinations,
where each consecutive appearance is simply, prev + 1,

so for 1, its 1,
for 1,1 its 1, 1+1,
for 1,1,1 its 1, 1+1, 2+1
so 3 combinations as its pairs and doesn't account for triplets or more,

we simply make a count hash for the elements,
we have another variable res,

res is simply, count hash starting at the next step,
our count hash builds from the 1st appearance,

res builds at the next appearance of the said character
this way we can skip elements that do not appear twice to be called as a pair,

and finally we return res which is simply the cumulative sum of every combination of a pair

time O(n)
space O(k) where k is number of unique elements.
