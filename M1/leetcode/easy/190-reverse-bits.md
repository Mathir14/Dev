Take n = 00000010100101000001111010011100 (in binary)
You want to return: 00111001011110000010100101000000

So bit at index 0 moves to 31, bit at 1 moves to 30, etc.

Key Idea
We process one bit at a time from the right end of n and push it to the left end of res.

Step-by-Step:
Start with res = 0.

Run a loop 32 times (because it’s a 32-bit number).

In each iteration:

Left shift res by 1 to make space for the new bit.

Take the last bit of n using n & 1.

OR it into res: res |= (n & 1)

Right shift n by 1 to drop the bit you just used.

Example Walkthrough
Say n = 13 → binary: 00000000000000000000000000001101

We’ll reverse those 32 bits:

Initial: res = 0

1st bit: n & 1 = 1 → res = 0 << 1 | 1 = 1

Next: n = 6, n & 1 = 0 → res = 1 << 1 | 0 = 2

Next: n = 3, n & 1 = 1 → res = 2 << 1 | 1 = 5

Next: n = 1, n & 1 = 1 → res = 5 << 1 | 1 = 11

Then rest are all 0s...

Final binary result will be: 10110000000000000000000000000000

Time & Space
Time: O(32) = O(1) → constant-time since input size is fixed (32 bits)
Space: O(1)
