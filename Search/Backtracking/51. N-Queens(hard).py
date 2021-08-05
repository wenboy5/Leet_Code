'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
'''

#time limit exceeded
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        check = []
        board = [["." for i in range(n)] for j in range(n)]
        test = [["." for i in range(n)] for j in range(n)]
        
        def fill(i,j,marker):
            test[i][j] = marker
            for co in range(1,n):
              
                for x,y in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]:
                    if 0<=(i+x*co)<n and 0<=(j+y*co)<n:
                        # print(i+x*co,j+y*co)
                        test[i+x*co][j+y*co] = marker

        def dfs(cnt,board,test,l):
            if cnt == n:
                to_be_add = deepcopy(board)
                if to_be_add not in check:
                    check.append(to_be_add)
                    ans.append(["".join(i) for i in to_be_add])
            else:
                for i in range(n):
                    for j in range(n):
                        if test[i][j] == ".":
                            board[i][j]="Q"
                            l.append((i,j))
                            fill(i,j,"X")
                            
                            dfs(cnt+1,board,test,l)
                            board[i][j] = "."
                            fill(i,j,".")
                            l.remove((i,j))
                            for x,y in l:
                                fill(x,y,"X")
        

        dfs(0,board,test,[])
        return ans
"""
Goal: Place a queen somewhere such that no queen are attacking each other
Approach: backtracking
- each recursive layer will decide on a row and also the placement of the queen
- the constraint is making sure we do not place a queen where its in sight of another queen. How?
    1) make sure it is not on the same column --> create a column set
    2) make sure it is not in same diagonal path --> create a diagonal set (calculated via r+c)
    3) make sure it is not in a antidiagonal path --> create a antidiagonal set (calculated via r-c)
    
    We dont need to worry about rows because it is handled by the backtracking parameter that always recurse
    to next level of the row
    
    ** note: if you dont know why r+c and r-c are diagonal paths --> Draw it out and check why it does!! 
    

"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        if n == 0: return []
        
        col = set()
        diagonal = set()    # determined by r+c
        antidiagonal = set() #
        output = []
        result = []
        
        def backtrack(r):
            nonlocal n,col,diagonal,antidiagonal,output,result
            if r == n:
                result.append(output[:])
                return
            
            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal: continue
                
                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                output.append('.'*c + 'Q' + '.'*(n-c-1))
                backtrack(r+1)
                
                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)
                output.pop()
        
        backtrack(0)
        return result