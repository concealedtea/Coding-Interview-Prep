class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def recur(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for x,y in directions:
                recur(grid, i+x, j+y)
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    recur(grid, i, j)
                    islandCount += 1
        return islandCount