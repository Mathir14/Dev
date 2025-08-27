Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Approach (cmp_to_key version)

Convert all numbers to strings.

Define a custom comparator:

Compare two numbers a and b by checking a+b vs b+a.

If a+b is larger, a should come before b.

If b+a is larger, b should come first.

If equal, order doesn’t matter.

Use cmp_to_key to convert the comparator for Python’s sort.

Join the sorted list into a single string.

If the first character is '0', return "0".

Approach (stretching strings version)

Convert all numbers to strings.

Sort them using a key: x\*10 (repeat each string 10 times to normalize lengths for comparison).

Sort in reverse to get descending order.

Join sorted strings.

If first character is '0', return "0".

Complexity

Time: O(n log n) for sorting.

Space: O(n) for string conversion and temporary lists.
