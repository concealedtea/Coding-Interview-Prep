"""
STATEMENT
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

CLARIFICATIONS
    An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.

EXAMPLE: 
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true

COMMENTS:
Determine the legality of the bracket matching. 
Use a stack to solve the problem (push and pop to stack to keep track of entries). 
When the left parenthesis is encountered, the right parenthesis is encountered, and the left parenthesis at the top of the stack is checked.
If it matches, the stack is returned. 
If it does not match, an error is returned. 
If the stack is empty and the right parenthesis is encountered, an error is returned.
After the traversal, if the stack is not empty, it also returns an error.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ")":
                if stack == [] or stack.pop() != "(":
                    return False
            elif s[i] == "]":
                if stack == [] or stack.pop() != "[":
                    return False
            elif s[i] == "}":
                if stack == [] or stack.pop() != "{":
                    return False
        if stack:
            return False
        else:
            return True