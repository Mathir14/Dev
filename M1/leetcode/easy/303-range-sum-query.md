Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

make a prefix sum array, but offset by 1 so prefix[i] means sum of first i elements (not index i, but count i)

helps avoid dumb edge cases

sumRange(l, r) just becomes prefix[r+1] - prefix[l]

clean, fast, and zero math mistakes

why this works:
prefix sum is gold when you're asked for repeated range queries

we frontload the cost in **init**, so each sumRange is O(1)

precompute tradeoff

time:
init: O(n)

query: O(1)
