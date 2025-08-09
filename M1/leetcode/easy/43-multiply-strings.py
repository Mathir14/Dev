# https://leetcode.com/problems/multiply-strings/description/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f"{int(num1) * int(num2)}"


# simply converted the strings into integers and returned their product, yeah works for now.
