Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

This function computes the maximum difference between successive elements in a list of numbers.

First, it sorts the input nums in ascending order so that consecutive elements are ordered.

It initializes gap to 0, which will track the largest difference found.

Using a pointer right starting at index 1, it iterates through the array:

At each step, it calculates the difference between the current element and the previous one.

If this difference is larger than the current gap, it updates gap.

The iteration continues until the end of the array.

Finally, it returns the largest gap found between consecutive elements.

This is a simple sorting-based approach to find the maximum consecutive difference.
