class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letterCounts = {}
        for letter in s:
            if letter not in letterCounts.keys():
                letterCounts[letter] = 1
            else:
                letterCounts[letter] += 1
        for letter in t:
            if letter not in letterCounts.keys():
                return False
            else:
                if letterCounts[letter] == 0:
                    return False
                else:
                    letterCounts[letter] -= 1
        for key in letterCounts:
            if letterCounts[key] != 0: return False
        return True