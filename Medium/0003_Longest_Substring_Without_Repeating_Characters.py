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
        return maxLen
        