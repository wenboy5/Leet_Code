'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        
        for i in range(nums[0],target+1):
            for each in nums:
                if i >= each:
                    dp[i] += dp[i-each]
                else:
                    continue
        return dp[target]



# time limit exceeded
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
      
        ans = 0
        def dfs(total):
            nonlocal ans
            if total == target:
                ans+=1
            elif total < target:    
                for i in nums:
                    if i <= target - total:
        
                        dfs(total+i)
        dfs(0)
        return ans