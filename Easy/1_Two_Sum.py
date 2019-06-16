"""
STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

CLARIFICATIONS
 - Each input has exactly 1 solution
 - The same element may not be used twice
 - The list is not empty
 - The list is not necessarily sorted

EXAMPLE: 
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

COMMENTS:
We can traverse the array and record the seen integers using a O(n) complexity set. set()
Iterate the list and at each step, look to see if there's a complement of the current item that exists in the set
O(n) time/space complexity
"""
class Solution(object):
    def twoSum(self, nums, target):
        s = set()
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if (complement in s):
                return [nums.index(complement),i]
            s.add(nums[i])
        return [0,0]