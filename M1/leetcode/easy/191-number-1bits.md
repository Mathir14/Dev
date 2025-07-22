Problem Statement
Write a function that takes an unsigned integer and returns the number of '1' bits (Hamming weight) it has.

Example
Input: n = 000001011  
Output: 3

Approach
Key Idea: Brian Kernighan's Algorithm
Subtracting 1 flips all bits after the rightmost set bit (including it).

Doing n & (n - 1) removes the lowest set bit.

Repeat this and count how many times it runs → gives the number of 1s.

Time & Space Complexity
Time: O(k), where k = number of set bits (max 32)

Space: O(1)
