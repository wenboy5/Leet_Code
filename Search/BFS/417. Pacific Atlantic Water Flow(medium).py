'''
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po = set()
        ao = set()
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            po.add((i,0))
            ao.add((i,n-1))
        for i in range(n):
            po.add((0,i))
            ao.add((m-1,i))
        po_reach = po.copy()
        ao_reach = ao.copy()
        def dfs(x,y,reachable):
            
            for p,q in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]: 
                if 0<=p<m and 0<=q<n and heights[p][q] >= heights[x][y] and (p,q) not in reachable:
                    reachable.add((p,q))
                    dfs(p,q,reachable)
        for i,j in po:
            dfs(i,j,po_reach)
            
        for i,j in ao:
            dfs(i,j,ao_reach)
        
        
        return list(po_reach.intersection(ao_reach))