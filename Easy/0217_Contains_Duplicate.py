class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for value in nums:
            if value in seen: return True
            else: seen.add(value)
        return False