class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.low, -num)
        heappush(self.high, -self.low[0])
        heappop(self.low)
        if len(self.low) < len(self.high):
            heappush(self.low, -self.high[0])
            heappop(self.high)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return float(self.high[0] - self.low[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Uses a min heap and a max heap to keep track of the values
# As long as there is an even number, take largest from maxHeap and smallest from minHeap and divide
# Otherwise, just take the largest value in the maxHeap