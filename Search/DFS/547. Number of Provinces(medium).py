'''
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        ans = 0
        
        def helper(i,j):
            for x in range(m):
                if isConnected[x][j] == 1:
                    isConnected[x][j] = 0
                    for p in range(n):
                        if isConnected[x][p] == 1:
                            helper(x,p)
        
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ans+=1
                    helper(i,j)
        return ans

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        ans = 0
        seen= set()
        def helper(i):
            for j, isfriend in enumerate(isConnected[i]):
                if isfriend and j not in seen:
                    seen.add(j)
                    helper(j)
            
        
        for i in range(m):
            if i not in seen:
                ans+=1
                helper(i)
                
        return ans