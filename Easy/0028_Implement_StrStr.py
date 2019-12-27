# Naive Implementation
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None: return 0
        needle_len = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1

# KMP Implementation 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
