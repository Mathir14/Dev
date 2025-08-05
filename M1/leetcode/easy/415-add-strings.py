# https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(100000)
        return f"{int(num1) + int(num2)}"


# add strings — problem expects manual string-based addition like school math but python makes it a joke
# just convert both strings to int, add, return as string

# used f-string to convert result to str
# `sys.set_int_max_str_digits()` is for really long strings; not needed here unless you're pushing crazy limits
