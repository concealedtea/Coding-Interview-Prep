class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0
        # Iterate through list
        while curr_idx < len(nums) - 1:
            # if the item currently monitored and the next element are duplicated, then delete the current item
            if nums[curr_idx] == nums[curr_idx+1]:
                del nums[curr_idx]
                curr_idx -= 1
            curr_idx += 1
        return len(nums)
            