class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        b1, b2, b1N, b2N, b2NCons, maxPick = None, None, 0, 0, 0, 0
        for fruit in tree:
            if fruit == b2:
                b2N, b2NCons = b2N + 1, b2NCons + 1
            elif fruit == b1:
                b1, b2, b1N, b2N, b2NCons = b2, b1, b2N, b1N+1, 1
            else:
                b1, b2, b1N, b2N, b2NCons = b2, fruit, b2NCons, 1, 1
            maxPick = max(maxPick, b1N+b2N)
        return maxPick