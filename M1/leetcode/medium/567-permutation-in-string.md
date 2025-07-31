Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

I need to find if any permutation of s1 exists in s2. Since it's a rearrangement, the frequency of characters should match. So I count frequency of s1 and compare it with every window of size len(s1) in s2.

Sliding window strategy:

Fixed-size window of length len(s1)

Count the frequency of s1 → hsh1

Count initial window in s2 → hsh2

Build hsh1 using s1

Build hsh2 using s2[:len(s1)]

If hsh1 == hsh2 → return True

Slide the window:

remove left character from hsh2

add right character into hsh2

if any char count hits 0, delete it

After each shift, compare with hsh1

Notes:

left was always 1 short because we’re removing the old element, so actual new window head is left+1

reused same “remove left, add right” logic from the previous problem

Counter is quick but not always efficient, better to build running freq if possible

I’ll try with ord() based array for speed next
