Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with linear runtime and constant extra space.

Approach
Key Idea: XOR
XOR (^) of a number with itself is 0.

XOR with 0 leaves the number unchanged.

Since all numbers except one appear twice, XORing all of them cancels the duplicates out, leaving only the unique number.

Time & Space Complexity
Time: O(n) — single pass through the list.
Space: O(1) — only one variable used.
