class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # base case
        if numRows == 1 or numRows == len(s): return s
        # 1 str for each row essentially
        rows = [''] * numRows
        idx, step = 0,1
        for ch in s:
            # add character to corresponding row string
            rows[idx] += ch
            # if we're at the top row, step sets to 1 (og case)
            if idx == 0: step = 1
            # if we're at the bottom row, reverse the step (go upwards)
            elif idx == numRows - 1: step = -1
            # increment row index
            idx += step
        # join all the rows
        return ''.join(rows)