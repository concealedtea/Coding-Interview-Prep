class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def typedString(s):
            newWord = []
            for char in s:
                if char != '#': 
                    newWord.append(char)
                elif newWord:
                    newWord.pop()
            return str(newWord)
        return typedString(S) == typedString(T)