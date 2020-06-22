class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key=lambda x: x[0]) # sort by start
        currEnd, minArrows = points[0][1], 1
        for point in points[1:]:
            if point[0] <= currEnd:
                currEnd = min(point[1], currEnd)
            else:
                currEnd = point[1]
                minArrows += 1
        return minArrows