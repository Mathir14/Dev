You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".

What I realized:

Wait so you remove right, which is the current window, because you want to only calculate what’s outside the window. Right is the inside — if you remove it from the whole string, only the outside remains.

The while loop is checking if the outside is now valid (balanced) after removing the current window. So the moment that happens, I know this current window can potentially be the answer. Now try to shrink from the left to get the minimum one that still satisfies the condition.

Why left stays at the point where it goes wrong:

Because left marks the beginning of the substring I’m removing. If I go past a point where the outside becomes unbalanced again, I’ve gone too far. So I expand right to remove more, and only shrink left if outside is still valid.

What makes this different from other sliding window problems:

Usually I’m building something inside the window — like a substring or sum. But here, it’s the opposite. I’m trying to get rid of the bad part. So the sliding window is _what I remove_, not what I include.

This feels backwards at first, but now it clicks.

Outside of window = full string minus current window.

The string is valid (i.e., balanced) when all outside char counts are ≤ target (length of string // 4). So while that’s true, I try to shrink the window.

The window represents the substring I will replace.
I expand `right` to remove more of the string.
I shrink `left` only if the outside part is still balanced.
The goal is to find the smallest such window.

Done.
