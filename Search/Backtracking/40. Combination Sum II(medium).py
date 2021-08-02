'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        c = candidates
        if sum(c) < target:
            return []
        c.sort()
        print(c)
        
        
        N = len(c)
        ans = []
        def dfs(n,i,l):
            if n == target and l not in ans:
                ans.append(l)
            else:
                for j in range(i,N):
                    if (n+c[j]) <= target:
                        if j>i and c[j] == c[j-1]:
                            continue
                        dfs(n+c[j],j+1,l+[c[j]])
        dfs(0,0,[])
        return ans