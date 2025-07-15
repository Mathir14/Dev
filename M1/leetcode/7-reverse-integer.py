# https://leetcode.com/problems/reverse-integer/description/

# this is a simple reverse the given integer problem

class Solution:
    def reverse(self, x: int) -> int:
        res = str(x)[::-1]
        if res[-1] == '-':
            res = res[-1]+res[:-1]
        res = int(res)
        return res if (-2**31) <= res <= (2**31 -1) else 0


# converted int value to string for easier operation
# reversed the string with [::-1]
# common issue: reversing a negative value such as -123 results in 321- when reversed
# used an if condition to check if the last character in the string is an '-'
# if it is, update the result string as, the -1 (last element '-' ) and the rest of the string before it res[:-1]
# that would be, '321-' as '-' + '321' being '-321'
# coverted it back into integer using int()
# the primary condition is to, check if the reversed integer is bigger than 32 bit integer 
# which ranges from -2^31 to 2^31 -1
# used precice value instead of bit_integer() as it may result in overflow in certain scenarios
# if it is smaller, return the reversed integer
# if it is bigger, return 0