'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0 
        for i in range(1,amount+1):
            for each in coins:
                if each <= amount:
                    dp[i] = min(dp[i], dp[i-each] +1)
        return -1 if dp[amount] == math.inf else dp[amount]
            

            
# time limit exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        print(coins)
        ans = math.inf
        def dfs(total,m):
            nonlocal ans
            if total == amount:
                #print("yes",m)
                if m < ans:
                    ans = m
            elif total < amount:    
                for i in coins:
                    if i <= amount - total:
                        #print(total+i,m+1)
                        dfs(total+i,m+1)
        dfs(0,0)
        if ans == math.inf:
            return -1
        return ans