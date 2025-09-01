Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Pick each index as a center.

Expand left and right while characters match.

Do this for both odd and even centers.

Track the longest palindrome seen.

Return that substring.
