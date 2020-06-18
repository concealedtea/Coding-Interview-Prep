class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def recursiveLandConversion(grid, i, j):
            # If invalid, return
            if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1'):
                return
            grid[i][j] = '0'
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            for x,y in directions:
                recursiveLandConversion(grid, i+x, j+y)
                
        if len(grid) == 0: return 0
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    recursiveLandConversion(grid, row, col)
                    islandCount += 1
        return islandCount