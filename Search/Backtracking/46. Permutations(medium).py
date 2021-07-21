'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = len(nums)
        if len(nums) == 1:
            return [nums]
        
        ans = []
        def dfs(n,l):
            if n == s:
                ans.append(l)
            else:
                for i in nums:
                    place = nums.index(i)
                    nums.remove(i)
                    dfs(n+1,l+[i])
                    nums.insert(place,i)
        
        dfs(0,[])
        return ans