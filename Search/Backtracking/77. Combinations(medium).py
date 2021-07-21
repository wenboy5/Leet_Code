'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1,n+1)]
        
        nums =[i for i in range(1,n+1)]
        
        ans = []
        def dfs(index,start,l):
            if index == k:
                ans.append(l)
            else:
                for i in range(start,n+1):
                    
                    dfs(index+1,i+1,l+[i])
                            
        dfs(0,1,[])
        return ans


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1,n+1)]
        
        nums =[i for i in range(1,n+1)]
        std = nums
        ans = []
        def dfs(n,l,nums):
            if n == k:
                ans.append(l)
            else:
                for i in nums:               
                    dfs(n+1,l+[i],std[i:])
                                 
        dfs(0,[],nums)
        return ans