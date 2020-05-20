import unittest
# O (nm) + O (m) + O(n) simplifies to O(nm)
# This is the fastest we can possibly get since we need to look at each element at least once

def zero_matrix(matrix):
    zeroRows, zeroCols = set(), set()
    n = len(matrix)
    m = len(matrix[0])
    # Get all rows and columns that have 0s in them
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                zeroRows.add(row)
                zeroCols.add(col)
    # Replace all rows
    for row in zeroRows:
        for i in range(m): matrix[row][i] = 0
    # Replace all columns
    for col in zeroCols:
        for i in range(n): matrix[i][col] = 0
    return matrix 

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()