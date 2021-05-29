'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        world = grid
        def flood(i,j):
            nonlocal world
            if world[i][j] == '1':
                world[i][j] = '0'
     
                if i+1<len(world):
                    flood(i+1,j)
                if j+1 < len(world[0]):
                    flood(i,j+1)
                if i-1 > -1:
                    flood(i-1,j)
                if j-1 > -1:
                    flood(i,j-1)
            
            
        for a in range(len(world)):
            for b in range(len(world[a])):
                if world[a][b] == '1':
                    number +=1
                    flood(a,b)
        return number

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        a,b = len(grid), len(grid[0])
        def landexist(grid):
            for sublist in grid:
                if "1" in sublist:
                    return True
            return False
        
        def findland(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        return i,j
        def adjcant(i,j):
            res = []
            for x, y in [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]:
                if x>=0 and x <=a-1 and y>= 0 and y<=b-1:
                    if grid[x][y] == "1":
                        grid[x][y] = "0"
                        res.append((x,y))
            return res
                    
        if not landexist(grid):
            return 0
        cnt = 0
        while(landexist(grid)):
            cnt += 1
            i, j = findland(grid)
            print("init",i,j)
            
            grid[i][j] = "0"
            
            
            temp = adjcant(i,j)
            print("len",len(temp))
            while temp:
                for i in range(len(temp)):
                    first = temp.pop(0)
                    temp += adjcant(first[0],first[1])
            
        return cnt
                
            