class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Explanation: Using a modified binary search, we are able to traverse until we find the first instance of the given target element, we then reproduce the 
        # binary search on the next largest integer
        def binarySearch(self, nums, target):
            firstPos = len(nums)
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) / 2
                if nums[mid] >= target: 
                    firstPos = mid
                    high = mid - 1
                else: 
                    low = mid + 1
            return firstPos
        targetFirstPos = binarySearch(self, nums, target)
        targetEndPos = binarySearch(self,nums,target + 1) - 1
        if targetFirstPos > targetEndPos: return [-1,-1]
        else: return [targetFirstPos, targetEndPos]
        