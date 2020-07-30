class Solution(object):
    def findDisappearedNumbers(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(arr)):
            currIDX = abs(arr[idx]) - 1
            arr[currIDX] = -abs(arr[currIDX])
        return [idx + 1 for idx in range(len(arr)) if arr[idx] > 0]
            