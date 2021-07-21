'''
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return False
        
        m,n= len(board),len(board[0])
        
        
        source = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    source.append((1,i,j,[(i,j)]))

        if len(word) == 1 and source != []:
            return True
        
        for each in source:   
            stack = [each]
            while stack:
                length, x,y, seen = stack.pop()
                
                for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<m and 0<=j<n and board[i][j] == word[length] and (i,j) not in seen:
                        
                        if length+1 == len(word):
                            return True
                        stack.append((length+1,i,j, seen+[(i,j)]))
        
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True
        
        m,n= len(board),len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    stack = [(1,i,j,[(i,j)])]
                    while stack:
                        length, x,y, seen = stack.pop()

                        for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if 0<=i<m and 0<=j<n and board[i][j] == word[length] and (i,j) not in seen:

                                if length+1 == len(word):
                                    return True
                                stack.append((length+1,i,j, seen+[(i,j)]))
        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True
        
        m,n= len(board),len(board[0])
        
        def dfs(index,x,y):
            if index == len(word):
                return True
            else:
                board[x][y], tmp = "", board[x][y]
                for i, j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<m and 0<=j<n and board[i][j] == word[index]:
                        if dfs(index+1,i,j):
                            return True
                board[x][y] = tmp
                
        counter, source = Counter(word), []
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] -= 1
                if board[i][j] == word[0]:
                    source.append((i,j))
                    
        if max(counter.values()) > 0: 
            return False
        
        for i,j in source: 
            if dfs(1,i,j):
                return True
        
        
        return False