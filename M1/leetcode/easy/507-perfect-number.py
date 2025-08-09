# https://leetcode.com/problems/perfect-number/description/


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                if i * i != num:
                    res += i + num // i
                else:
                    res += i
        return res == num
