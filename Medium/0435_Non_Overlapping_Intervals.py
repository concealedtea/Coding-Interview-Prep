class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        currEnd = intervals[0][1]
        countRemovals = 0
        for interval in intervals[1:]:
            if interval[0] < currEnd:
                countRemovals += 1
                currEnd = min(interval[1], currEnd)
            else: 
                currEnd = interval[1]
        return countRemovals