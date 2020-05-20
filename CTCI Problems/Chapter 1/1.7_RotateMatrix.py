import unittest
# O(N * N)
# First transposes the matrix, swaps the rows and the columns
def rotate_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            # this if clause is so that they aren't accidentally swapped back later
            if row < column:
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    for row in matrix: row.reverse()
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()