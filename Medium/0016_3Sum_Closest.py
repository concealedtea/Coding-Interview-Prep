class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            aPoint = i + 1
            bPoint = len(nums) - 1
            while aPoint < bPoint:
                totSum = nums[i] + nums[aPoint] + nums[bPoint]
                if totSum == target: 
                    return totSum
                elif totSum < target: 
                    aPoint += 1
                else: 
                    bPoint -= 1
                if abs(totSum - target) < abs(result - target): 
                    result = totSum
        return result