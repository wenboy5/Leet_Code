'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        new = [[0 for i in range(n)] for j in range(m)]
        
        new[0][0] = grid[0][0]
        for i in range(1,m):
            new[i][0] = grid[i][0] + new[i-1][0]
        for i in range(1,n):
            new[0][i] = grid[0][i] + new[0][i-1]
        
        for i in range(1,m):
            for j in range(1,n):
                new[i][j] = min(new[i][j-1] , new[i-1][j]) + grid[i][j]
                
        return new[m-1][n-1]