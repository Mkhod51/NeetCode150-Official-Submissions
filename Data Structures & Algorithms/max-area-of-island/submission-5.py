class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            
            if not ((0 <= x < len(grid)) and (0 <= y < len(grid[0]))):
                return 0
            
            if grid[x][y] == 0:
                return 0 

            grid[x][y] = 0

            return (
            1 + 
            dfs(x-1,y) + 
            dfs(x+1,y) + 
            dfs(x,y-1) + 
            dfs(x,y+1) ) 

        curMax = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1: 
                    curMax = max(curMax, dfs(x,y))
                
        return curMax