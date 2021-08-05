'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        dp = [0] * (n-1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        
        c = nums[::-1]
        dp2 = [0] * (n-1)
        dp2[0],dp2[1] = c[0], max(c[0],c[1])
        
        for i in range(2,n-1):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            dp2[i] = max(dp2[i-2]+c[i],dp2[i-1])
        return max(dp[n-2],dp2[n-2])