A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false

````markdown
# Perfect Number Check — Condensed Code (User Style)

```python
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                res += i
                if i != num // i:
                    res += num // i
        return res == num
```
````

Returns `True` if `num` is a perfect number (sum of divisors excluding itself equals `num`), else `False`.
Early return `False` for `num == 1`.
Starts sum at 1 since 1 divides every number > 1.
Loops through possible divisors from 2 up to `√num`.
If `i` divides `num`, add both divisors `i` and `num // i`, avoiding double-counting for perfect squares.
Finally compares sum of divisors `res` to `num`.

Time: O(√n)
Space: O(1)
