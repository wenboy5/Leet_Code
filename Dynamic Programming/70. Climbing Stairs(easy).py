'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#Time limit exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        cnt = 0
        
        def dfs(start):
            nonlocal cnt
            if start == n:
                cnt+=1
            elif start < n:
                dfs(start+1)
                dfs(start+2)
        dfs(0)
        return cnt

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: 
            return 1
        i = 2
        dp = {0: 1,
			  1: 1} #Base case DP table
        while i < n+1:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]