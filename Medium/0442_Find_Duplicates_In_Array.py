class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for idx in range(len(nums)):
            currIDX = abs(nums[idx]) - 1
            if nums[currIDX] < 0: ans.append(currIDX + 1)
            nums[currIDX] = -nums[currIDX]
        return ans