Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Use a set to track numbers we’ve already seen.

If n becomes 1, return True.

If n repeats (appears in seen), that means we’re in a cycle → return False.

Update n each step as the sum of squares of its digits.

Time: O(log n) per iteration (since number of digits in n is log n).

Space: O(log n) due to the seen set storing previously computed numbers.
