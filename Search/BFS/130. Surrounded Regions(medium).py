'''
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        checked = set()
        
        def bfs(x,y):
            if (x,y) not in checked:
                checked.add((x,y))
                for p,q in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]: 
                    if 0<=p<m and 0<=q<n and board[p][q] == "O" and (p,q) not in checked:
                        bfs(p,q)
        for i in range(n):
            if board[0][i] == "O":
                bfs(0,i)
            if board[m-1][i] == "O":
                bfs(m-1,i)
                
        for i in range(m):
            if board[i][0] == "O":
                bfs(i,0)
            if board[i][n-1] == "O":
                bfs(i,n-1)
                
        for i in range(m):
            for j in range(n):
                if (i,j) in checked:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"