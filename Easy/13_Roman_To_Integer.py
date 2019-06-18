"""
STATEMENT
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

CLARIFICATIONS
    - An input is a palindrome only if it reads the same backwards and forwards
    - A negative number can never be a palindrome
    - Any singular number is automatically a palindrome

EXAMPLE: 
Input: 121
Output: true
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

COMMENTS:
Determine if number is < 0 (non-palindrome) or if number is both >= 0 and < 10 (palindrome)
We can effectively remove the all but the ones digit of a number by performing a  "% 10"  on it
We can also remove the ones digit of a number by performing a "// 10" operation
In this manner, we are able to efficiently reverse the number and store a copy of said reversed number
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x 
        reverse = 0
        while (x > 0):
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        return reverse == temp