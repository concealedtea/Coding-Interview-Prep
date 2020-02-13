class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ints = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        romans = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        finalString = ""
        for i in xrange(12,-1,-1):
            finalString += num // ints[i] * romans[i]
            num %= ints[i]
        return finalString