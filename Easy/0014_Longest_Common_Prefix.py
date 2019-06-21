"""
STATEMENT
Write a function to find the longest common prefix string amongst an array of strings.

CLARIFICATIONS
    - If there is no common prefix, return an empty string "".
    - All given inputs are in lowercase letters a-z.

EXAMPLES:
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

COMMENTS:
The easiest way to solve this problem is to just iterate and check each character at the index
Can be done with substrings and Python's built in function 'startswith()'

Other method is to first find the smallest string in the array, 

"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        shortest = min(strs, key=len)
        for index, ch in enumerate(shortest):
            for other in strs:
                if other[index] != ch:
                    return shortest[:index]
        return shortest