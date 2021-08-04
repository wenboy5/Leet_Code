'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        nums.sort()
        N = len(nums)
        ans = []
        def dfs(i,j,n,l):
            if n == i and l not in ans:
                ans.append(l)
            else:
                for q in range(j,N):
                    dfs(i,q+1,n+1,l+[nums[q]])
        for q in range(N+1):
            dfs(q,0,0,[])
        return ans