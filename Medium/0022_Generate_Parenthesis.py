# Uses O(n!) time, very inefficient but it is the main method to solve this problem
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backTracking(outputArr, currString, maxParens, openP, closeP):
            # Some Base Case, add value to array
            if len(currString) == maxParens * 2:
                outputArr.append(currString)
                return
            # Rest of decisions
            if openP < maxParens: 
                backTracking(outputArr, currString + '(', maxParens, openP + 1, closeP)
            if closeP < openP: # Can't have close before open
                backTracking(outputArr, currString + ')', maxParens, openP, closeP + 1)
            
        # Call backtracking
        outputArr = []
        backTracking(outputArr, '', n , 0, 0)
        return outputArr