'''
you are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0

'''

'''
Overall, we run an iteration over the sequence of prices.

Over the iteration, we calculate 4 variables which correspond to the costs or the profits of each action respectively, as follows:

t1_cost: the minimal cost of buying the stock in transaction #1. The minimal cost to acquire a stock would be the minimal price value that we have seen so far at each step.

t1_profit: the maximal profit of selling the stock in transaction #1. Actually, at the end of the iteration, this value would be the answer for the first problem in the series, i.e. Best Time to Buy and Sell Stock.

t2_cost: the minimal cost of buying the stock in transaction #2, while taking into account the profit gained from the previous transaction #1. One can consider this as the cost of reinvestment. Similar with t1_cost, we try to find the lowest price so far, which in addition would be partially compensated by the profits gained from the first transaction.

t2_profit: the maximal profit of selling the stock in transaction #2. With the help of t2_cost as we prepared so far, we would find out the maximal profits with at most two transactions at each step.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        # pad the right DP array with an additional zero for convenience.
        right_profits = [0] * (length + 1)

        # construct the bidirectional DP array
        for l in range(1, length):
            left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r+1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        max_profit = 0
        for i in range(0, length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

        return max_profit