# https://leetcode.com/problems/sqrtx/description/


# built-in function
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


# math sqrt
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


# newton's method
def sqrt_newton(n):
    if n < 2:
        return n
    x = n
    while x * x > n:
        x = (x + n // x) // 2
    return x
