class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix) if matrix else 0, len(matrix[0]) if matrix else 0
        atl, pac, M, N = set(), set(), range(0, m), range(0, n)

        def dfs(i, j, w):
            for c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if c[0] in M and c[1] in N and c not in w and matrix[c[0]][c[1]] >= matrix[i][j]:
                    w.add(c)
                    dfs(c[0], c[1], w)

        for rows, cols, w in [(M,[0],pac), (M,[n-1],atl), ([0],N,pac), ([m-1],N,atl)]:
            for i, j in product(rows, cols):
                w.add((i,j))
                dfs(i, j, w)

        return atl & pac