class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        aPointer, bPointer = 0, len(height) - 1
        while aPointer < bPointer:
            minHeight = min(height[aPointer], height[bPointer])
            width = bPointer - aPointer
            if height[aPointer] < height[bPointer]:
                maxArea = max(maxArea, minHeight * width)
                aPointer += 1
            else:
                maxArea = max(maxArea, minHeight * width)
                bPointer -= 1
        return maxArea