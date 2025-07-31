Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Same idea as permutation in a string but now I return all starting indices where an anagram of p appears in s.

Sliding window logic:

Fixed window of size len(p)

Count freq of p using Counter → hp

Count initial window in s → hs

If hp == hs, append 0 to result

Loop through s from index len(p):

Remove s[left] from hs (decrement, delete if 0)

Add s[right] to hs (increment)

Move left forward by 1

If hp == hs → append left (because left points to previous head)

Notes:

Reused the same "remove left, add right" logic from the previous problem

left is the new window start after removing the old left

Counter works, but for more speed maybe try using a fixed-size array with ord() later
