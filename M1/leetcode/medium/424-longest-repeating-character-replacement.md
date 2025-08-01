You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

so we’re given a string and a k, we can replace at most k characters to form the longest possible uniform substring. by uniform i mean all same characters.

i don’t actually do replacements, i just track frequencies. i move right, and for each window, i calculate how many chars i’d need to replace to make everything in the window same. that’s (window size - max freq char). if that’s more than k, i shrink the window from the left.

i keep maxf which is the frequency of the most common char in the window, and i don’t update it while shrinking because even if it’s stale, the window will still be invalid when needed, so logic still holds.

i just keep updating the result with the max valid window length.

this whole thing became a template: move right, update frequency, check condition, if invalid, shrink left, keep track of max result.
