Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

function finds the length of the longest consecutive sequence in a list of numbers.

It first handles an empty list by returning 0.

Duplicate numbers are removed with set(nums) and the remaining numbers are sorted.

Two counters are used:

current tracks the length of the ongoing consecutive sequence.

length stores the maximum sequence length found so far.

The function iterates through the sorted numbers starting from index 1:

If the current number is exactly 1 greater than the previous, it increments current and updates length if necessary.

If the sequence is broken, current is reset to 1.

Finally, it returns length, which represents the length of the longest consecutive sequence in the input
