# Shifting Window Technique
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxLen = 0
        # Non repeating characters
        seen = set()
        while right < len(s):
            # if not seen, shift right pointer (expand) and recheck maxLength
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                maxLen = max(maxLen, right - left)
            # if already seen, remove item at the left pointer from the seen and shift left pointer (shift)
            else: 
                seen.remove(s[left])
                left += 1
        # return maxLen
        return maxLen
        
    # Alternative method to implement using index
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        maxLen = start = 0
        for idx, value in enumerate(s):
            if value in dictionary:
                sums = dictionary[value] + 1
                if sums > start:
                    start = sums
            num = idx - start + 1
            if num > maxLen:
                maxLen = num
            dictionary[value] = idx
        return maxLen