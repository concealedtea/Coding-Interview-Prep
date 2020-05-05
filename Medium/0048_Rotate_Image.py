
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # First transpose the matrix, replace row 1 with column 1, row 2 with column 2, etc.
        for row in xrange(len(matrix)):
            for column in xrange(len(matrix)):
                if row < column:
                    matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        for row in matrix: row.reverse()
        return matrix
