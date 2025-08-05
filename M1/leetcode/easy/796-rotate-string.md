Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

loop through s, rotate one char at a time (move first to end)
after each rotation, check if it matches goal

if match found, return True

after full rotation cycle, if nothing matched, return False
simple brute-force rotation logic – works fine for small strings
