class Solution(object):
    def characterReplacement(self, s, k):
        d = collections.defaultdict(int)
        start, maxLen, maxCount = 0, 0, 0
        for end in range(len(s)):
            d[s[end]] += 1
            maxCount = max(maxCount, d[s[end]])
            while end - start + 1 - maxCount > k:
                d[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen
                
                