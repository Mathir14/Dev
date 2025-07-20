# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        res = str(x)
        return res == res[::-1]

# converted the integer to string
# compared the string with its reverse

# adjustments
# added edgecase (x < 0) for negative values
# avoids extra operations