# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int) -> int:

        if n < 2:
            return n

        f1, f2 = 0, 1
        temp = 0

        for i in range(2, n + 1):
            temp = f1 + f2
            f1 = f2
            f2 = temp

        return temp
