class Solution:
    # Since it's a sorted array, we just need to insert once we find a value that's higher
    # Linear search w/ O(n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] >= target: return i
        return len(nums)

    # Binary search w/ O(logn)
    # This is better asymptotically due to a lower O(logn)
    def searchInsert2(self,nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (int) ((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else: low = mid + 1
        return low

