class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        intersections = []
        pointerA, pointerB = 0, 0
        while pointerA < len(A) and pointerB < len(B):
            currA, currB = A[pointerA], B[pointerB]
            aStart, aEnd = currA[0], currA[1]
            bStart, bEnd = currB[0], currB[1]
            if aStart <= bEnd and bStart <= aEnd:
                startIntersection = max(aStart, bStart)
                endIntersection = min(aEnd, bEnd)
                intersections.append([startIntersection, endIntersection])
            if aEnd <= bEnd: pointerA += 1
            else: pointerB += 1
        return intersections
            
            