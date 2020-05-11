class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        base = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= base
            base *= nums[i]
        base = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= base
            base *= nums[i]
        return output