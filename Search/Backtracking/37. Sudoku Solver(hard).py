'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        n = len(board)
        a = {i for i in "123456789"}
        
        print(a)
        
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    cell = board[i][j]
                    rows[i].add(cell)
                    cols[j].add(cell)
                    boxes[(i//3),(j//3)].add(cell)
        
        def find():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == ".":
                        return i, j
            return -1, -1
            
        def dfs(board):
            i, j = find()
            if i==-1 and j == -1:
                return True
            
            known = set()
            known.update(rows[i],cols[j],boxes[(i//3),(j//3)])
            c = a - known

            for each in c:
                board[i][j] = each
                rows[i].add(each)
                cols[j].add(each)
                boxes[(i//3),(j//3)].add(each)
                if dfs(board):
                    return True
                board[i][j] = "."
                rows[i].remove(each)
                cols[j].remove(each)
                boxes[(i//3),(j//3)].remove(each)
            return False
        dfs(board)