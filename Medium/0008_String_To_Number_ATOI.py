class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        intValue,sign,signed = 0,1,0
        for idx,ch in enumerate(str):
            if ch == ' ' and signed == 0: intValue += 0
            elif ch.isnumeric():
                # ord returns the unicode position of the character (10-0)
                intValue = intValue * 10 + ord(ch) - ord('0')
                signed = 1
            elif ch == '+' and signed == 0: sign,signed = 1,1
            elif ch == '-' and signed == 0: sign,signed = -1,1
            else: break
        return max(-2**31, min(sign * intValue,2**31 - 1))