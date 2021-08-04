'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        N = len(nums)
        ans = []
        def dfs(i,j,n,l):
            if n == i:
                ans.append(l)
            else:
                for q in range(j,N):
                    dfs(i,q+1,n+1,l+[nums[q]])
        for q in range(N+1):
            dfs(q,0,0,[])

        return ans
        