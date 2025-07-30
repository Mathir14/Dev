Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

we're given a string, need to find the longest substring with all unique characters, so no repeats allowed in the current window

brute force would be checking all substrings and testing for repeats but that’s too slow, so we use sliding window + set

we keep a left and right pointer, both starting at 0
char set keeps track of what’s in the current window

right expands the window
if s[right] is already in the set, it means duplicate found, so we shrink the window from the left

now we don’t just nuke the entire window and reset everything
we remove one element at a time from the left until s[right] is no longer in the set
this way we keep the valid part of the window and slide forward

each time we expand or shrink, we update length if the current window (right - left + 1) is bigger

example:
abcdeac
go till e — all unique
then comes a — already in set
so start removing from left — a out, now window is bcdea
right moves to c — again in set
repeat: remove b, then c
now valid window is dea
keep going

this method never resets the whole set, just adjusts it efficiently using sliding window
and we get the longest substring with unique characters in O(n)
