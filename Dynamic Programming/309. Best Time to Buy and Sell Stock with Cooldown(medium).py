'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# initialization
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n == 0 or n == 1:
            return 0
        
        dp = [0 for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1,i):
                #print("start", i,j,i-j)
                if prices[i-1] - prices[j-1] > 0:
                    #print("inside", i-1,prices[i-1],j-1,prices[j-1],dp[j-2])
                    if j-2 > 0:
                        dp[i] = max(dp[i], dp[j-2] + prices[i-1] - prices[j-1] )
            if i >= 2:
                dp[i] = max(max(dp[:i+1]) , prices[i-1] - min(prices[:i-1]))
                    
        print(dp)
        return max(dp)

