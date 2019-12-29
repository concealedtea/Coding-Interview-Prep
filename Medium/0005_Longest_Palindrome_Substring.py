class Solution(object):
                    
    def longestPalindrome(self, s):
        # Manacher's Algorithm
        right = center = 0
        # Temporary array to store values even after we adjust for even-len palindromes
        temp = s
        # By adding in filler characters, we're able to detect any even-length palindromes
        s = '#'.join('^{}$'.format(s))
        palinarray = [0] * len(s)
        # Iterate through s
        for i in range(1, len(s) - 1):
            palinarray[i] = (right > i) and min(right - i, palinarray[2*center - i])
            while s[i + 1 + palinarray[i]] == s[i - 1 - palinarray[i]]:
                palinarray[i] += 1
            if i + palinarray[i] > right:
                center, right = i, i + palinarray[i]
        # n = length of substring, i = center index
        maxLen, centerIndex = max((n, i) for i, n in enumerate(palinarray))
        # check back to original substring to find the substring between the 2 limits
        return temp[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]