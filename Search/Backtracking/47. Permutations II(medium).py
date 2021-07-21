'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = len(nums)
        if len(nums) == 1:
            return [nums]
        
        ans = set()
        def dfs(n,l):
            if n == s and tuple(l) not in ans:
                ans.add(tuple(l))
            else:
                for i in nums:
                    place = nums.index(i)
                    nums.remove(i)
                    dfs(n+1,l+[i])
                    nums.insert(place,i)
        
        dfs(0,[])
        return list(ans)