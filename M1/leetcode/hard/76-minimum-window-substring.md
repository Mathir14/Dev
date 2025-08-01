Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

so i’m given s and t. i need to find the smallest substring in s that contains all characters from t, with correct frequencies. not just presence — if t has 2 a’s, the window must have 2 a’s too.

i started by building a target map — just a frequency count of all chars in t.

then i started moving a right pointer over s, expanding the window and updating a window map for current char counts.

whenever a char’s count in window matched what target needed, i increased have. once have == need (which means the window contains all unique chars from t with correct counts), i knew it was a valid window.

then i tried shrinking from the left — always trying to minimize the window size while keeping it valid. while shrinking, i kept checking if the current window was the best so far. if yes, i stored the left and right bounds in res and updated rlen.

initial mistake i made — i was only tracking the length of the smallest window but not the actual left and right bounds, so when returning the result, i used wrong slicing like s[left:res+1] which broke things. also, i forgot to reduce have when shrinking caused the window to lose a needed char, so my have == need check was giving wrong results.

fixed that by:

keeping res = [left, right] instead of just storing length

properly updating have -= 1 when shrinking removes a needed char

returning s[res[0]:res[1]+1] only if rlen != inf

also skipped using collections.Counter() because i wanted full control and didn’t want overhead — stuck with plain dicts.

final logic: build target, expand right, update window counts, when valid (have == need), try shrinking from left, update result window if it’s smaller, return the substring using stored bounds.

it became just another version of the sliding window pattern — expand right, check validity, shrink left, repeat.
