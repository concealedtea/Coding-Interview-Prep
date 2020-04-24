class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            # Must use tuple since list is mutable
            key = tuple(sorted(word))
            anagrams[key] = anagrams.get(key, []) + [word]
        return anagrams.values()