Problem
Given two integers left and right, return the bitwise AND of all numbers in the inclusive range [left, right].

Core Insight
Any bit that changes in the range [left, right] will become 0 in the final result.

So the only bits that survive in the result are the common leftmost prefix of left and right.

Why?
Let’s say:

left = 011001010100
right = 011001111111

Notice the prefix 011001 is the same.
Everything after that differs — so ANDing those varying bits will give 0.

We just need to find this common prefix, and then shift it back to form the final number.

Approach
Keep right-shifting left and right until they become equal.

Every shift removes one bit from the end — you’re shrinking the range.

Keep track of how many times you shifted.

Once left == right, you’ve isolated the common prefix.

Left-shift it back by the same number of times to restore zeros at the end.

Example
Input: left = 5, right = 7
Binary:
5 = 101
6 = 110
7 = 111

Result:

101 & 110 & 111 = 100 → 4

How it works:

5 and 7 → not equal

5>>1 = 2, 7>>1 = 3 → not equal

2>>1 = 1, 3>>1 = 1 → equal

Shift count = 2

Final result: 1 << 2 = 4

Time & Space
Time: O(1) — Max 32 shifts
Space: O(1)
