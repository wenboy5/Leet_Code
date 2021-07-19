'''

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        
        def helper(x,y):
            nonlocal score
            grid[x][y] = 0
            score += 1
            for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (0<= i<m) and (0<=j<n) and grid[i][j] == 1:
                    
                    helper(i,j)
            return score
                    
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    score = 0
                    local = helper(row,col)
                    ans = max(ans,local)
                    
        
        return ans
        
        