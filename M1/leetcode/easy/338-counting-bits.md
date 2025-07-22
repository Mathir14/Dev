Problem Statement
Given an integer n, return an array ans where ans[i] is the number of 1 bits in the binary representation of i, for all i in the range [0, n].

Key Insight
Let’s say you already know how many set bits are in i // 2.
Then for i, there are two parts to consider:

i >> 1 → basically i // 2, right-shifting one bit

i & 1 → tells you if the least significant bit is 1 (odd number) or 0 (even)

So the idea is:

countBits[i] = countBits[i >> 1] + (i & 1)
Why does this work?
Right-shifting i just removes the last bit.

(i & 1) checks whether that bit was a 1.

So you're reusing the result of a smaller subproblem (i >> 1) and just adding the LSB.

Example Breakdown
Say i = 5 → binary is 101

i >> 1 = 2 → binary: 10

i & 1 = 1 (because LSB is 1)

So:

countBits[5] = countBits[2] + 1
And we already know countBits[2] = 1
→ So, countBits[5] = 1 + 1 = 2

Time & Space Complexity
Time: O(n)
Space: O(n)
