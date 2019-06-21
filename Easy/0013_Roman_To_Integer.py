"""
STATEMENT
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

CLARIFICATIONS
    - Any letter is representative of the number it represents unless it is followed by a larger number, in which case the two's difference is added instead

EXAMPLE: 
Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "IX"
Output: 9

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
COMMENTS:
We should first define a dictionary to return the numerical value of any character, this will make valuation much easier. 
We then iterate through the string, starting at index 0 and going through.
If the next character is of larger value, then add the current number and subtract the next number twice
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum = 0
        for i in range(0, len(s)):
            if i > 0 and numerals[s[i]] > numerals[s[i-1]]:
                sum += numerals[s[i]] - numerals[s[i-1]] * 2
            else:
                sum += numerals[s[i]]
        return sum
    