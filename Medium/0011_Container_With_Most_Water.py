class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = 0
        width = len(height) - 1
        for w in range(width, 0, -1):
            if height[left] < height[right]:
                water, left = max(water, height[left] * w), left + 1
            else:
                water, right = max(water, height[right] * w), right - 1
        return water