'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

#method 1 dp
'''
In the previous part, we introduced an intuitive idea from brute force to dp method, and here we need to decide the details of the algorithm.

We can either store the dp results in a dict or an array. Array costs less time for accessing and updating than dict, so we always prefer an array when possible. Because of three needed characteristics (day number, transaction number used, stock holding status), a three-dimensional array is our choice. We can use dp[day_number][used_transaction_number][stock_holding_status] to represent our states, where stock_holding_status is a 0/1 number representing whether you hold the stock or not.

The value of dp[i][j][l] represents the best profit we can have at the end of the i-th day, with j remaining transactions to make and l stocks.

The next step is finding out the so-called "transition equation", which is a method that tells you how to jump from one state to another.

We start with dp[0][0][0] = 0 and dp[0][0][1]=-prices[0], and our final aim is max of dp[n-1][j][0] from j=0 to j=k. Now, we need to fill out the entire array to find out the result. Assume we have gotten the results before day i, and we need to calculate the profit of day i. There are only four possible actions we can do on day i: 1. keep holding the stock, 2. keep not holding the stock, 3. buy the stock, or 4. sell the stock. The profit is easy to calculate.

Keep holding the stock:
dp[i][j][1] = dp[i-1][j][1]dp[i][j][1]=dp[i−1][j][1]

Keep not holding the stock:
dp[i][j][0] = dp[i-1][j][0]dp[i][j][0]=dp[i−1][j][0]

Buying, when j>0:
dp[i][j][1] = dp[i-1][j-1][0]-prices[i]dp[i][j][1]=dp[i−1][j−1][0]−prices[i]

Selling:
dp[i][j][0] = dp[i-1][j][1]+prices[i]dp[i][j][0]=dp[i−1][j][1]+prices[i]

We can combine they together to find the maximum profit:

dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])dp[i][j][1]=max(dp[i−1][j][1],dp[i−1][j−1][0]−prices[i])

dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])dp[i][j][0]=max(dp[i−1][j][0],dp[i−1][j][1]+prices[i])

Awesome! Now we can use for-loop to calculate the whole dp array and achieve our final result. Remember to solve the special cases when 2k > n.
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k==0:
            return 0

        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k+1):
                # transition equation
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        res = max(dp[n-1][j][0] for j in range(k+1))
        return res


#method 2 kadane‘s algorithm
'''
Take [2,3,5,1,4,8,6,4,9] and k=3 as example

all pnl[[i] is initiated to 0,
after the 1st loop, all pnl[i] is set to get the largest profit up to i-th in 1 subarray.
So pnl = [0,1,3,3,3,3,7,7,7,8] after the first loop.
in the second loop, it means we can choose at most two contiguous subarray for largest profit.
In 4-th day, we can choose [2,3,5],[1,4] as the two subarrays, then pnl[4] = 6
In the 8th day, we'll choose [1,8][4,9] as the two subarrays, then pnl[8] = 12 (the [2,3,5] is discard)
So pnl = [0,1,3,3,6,10,10,10,12]
in the 3th loop, the pnl is almost the same as previous, but we can pick the discard subarray for 8-th
pnl = [0,1,3,3,6,10,10,10,15]
the final result is 15
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2*k >= len(prices): 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        
        pnl = [0]*len(prices)
        for _ in range(k):
            val = 0
            for i in range(1, len(pnl)): 
                val = max(pnl[i], val + prices[i] - prices[i-1]) 
                pnl[i] = max(pnl[i-1], val)
        return pnl[-1]


#time limit exceeded
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ans = 0
        
        def dfs(n,profit,curr,l):
            nonlocal ans
            if n == k or l == []:
                ans = max(ans,profit)
            elif n < k:
                if curr == -1 or l[0] <= curr:
                    curr = l[0]
                    if len(l) == 1:
                        #print("case1",n,profit,curr,[])
                        dfs(n,profit,curr,[])
                    else:
                        #print("case2",n,profit,curr,l[1:])
                        dfs(n,profit,curr,l[1:])
                elif l[0] > curr:
                    if len(l) == 1:
                        #print("case3",n+1,profit+l[0]-curr,-1,[])
                        dfs(n+1,profit+l[0]-curr,-1,[])
                    else:
                        if len(l) >= 2:
                            #print("case4",n,profit,curr,l[1:])
                            dfs(n,profit,curr,l[1:])
                        #print("case5",n+1,profit+l[0]-curr,-1,l[1:])
                        dfs(n+1,profit+l[0]-curr,-1,l[1:])
        dfs(0,0,-1,prices)
        return ans