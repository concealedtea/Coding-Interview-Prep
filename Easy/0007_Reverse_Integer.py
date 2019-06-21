"""
STATEMENT
Given a 32-bit signed integer, reverse digits of an integer.

CLARIFICATIONS
    - Any number is reversed
    - Any negative number keeps the negative sign at the start
    - Any 0s at the end are converted into no number
    - If x is not within [2^31, -2^31], then return 0

EXAMPLES:
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

COMMENTS:
This question can be solved using a modulo and division operation, we are essentially going through and dividing each number until all the digits are reversed
However it's much more efficient to solve using a conversion to string and reverse array [::-1]
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            x = x * -1
            reverse = str(x)
            answer = int(reverse[::-1].lstrip("0")) * -1
            if answer > 2**31 - 1 or answer < -(2**31):
                return 0
            else:
                return answer
        else:
            reverse = str(x)
            answer = int(reverse[::-1].lstrip("0"))
            if answer > 2**31 - 1 or answer < -(2**31):
                return 0
            else:
                return answer

        # Method of non-converting to string
        # if x < 0:
        #     x = x * -1
        #     temp = x 
        #     reverse = 0
        #     while (x > 0):
        #         digit = x % 10
        #         reverse = reverse * 10 + digit
        #         x = x // 10
        #     if reverse > 2**31 - 1 or reverse < -(2**31):
        #         return 0
        #     else:
        #         return reverse * -1
        # else: 
        #     temp = x 
        #     reverse = 0
        #     while (x > 0):
        #         digit = x % 10
        #         reverse = reverse * 10 + digit
        #         x = x // 10
        #     if reverse > 2**31 - 1 or reverse < -(2**31):
        #         return 0
        #     else:
        #         return reverse

        