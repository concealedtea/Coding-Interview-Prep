class Solution(object):
    def minWindow(self, s, t):
        
        # Declare a frequency dictionary for every character
        dict = collections.Counter(t)
        left, satisfied = 0, 0
        result = ""
        target_len = len(t)
        
        # Go through every chacracter in s
        for right in range (len(s)):
            if dict[s[right]]>0: # If its in dictionary
                satisfied+=1 # increase satisfied
            dict[s[right]]-=1 # Remove it from dictionary
            
            while satisfied == len(t): # Keep removing left values till we are satisified
                if not result or right - left +1 <len(result): # store the samllest result always
                    result = s[left: right+1]
                    
                dict[s[left]]+=1 # Add it back to dictionary
                if dict[s[left]]>0: # If it was a part of dictionary and has been added back
                    satisfied-=1 # decrease satisfied
                left+=1 # Try removing next left value
            
        return result
