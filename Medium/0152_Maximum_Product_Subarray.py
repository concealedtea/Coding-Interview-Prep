class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = currMin = totalMax = nums[0]
        for i in range(1, len(nums)):
            temp = currMax
            currMax = max(max(currMax * nums[i], currMin * nums[i]), nums[i])
            currMin = min(min(temp * nums[i], currMin * nums[i]), nums[i])
            if currMax > totalMax: totalMax = currMax
        return totalMax
            