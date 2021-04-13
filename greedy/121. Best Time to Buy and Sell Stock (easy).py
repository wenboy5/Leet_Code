'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        # brute force
        # times out on large test case
        max_profit = 0
        for i in range(len(prices) - 1):
            maxRight = max(prices[i + 1:])
            max_profit = max(maxRight - prices[i], max_profit)
            
        
        return max_profit
        """
        """
        # one pass
        # faster that 20%, better memory than 95%
        # keep track of lowest int seen so far and calculate diff between that and current price
        lowest = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            lowest = min(prices[i], lowest)
            max_profit = max(prices[i] - lowest, max_profit)
        
        return max_profit
        """
        # stolen from fastest submissions
        # One pass, O(n) time and O(1) space
        # this is a little faster because it doesn't do two calculations per iteration.
        # it also doesn't access the list multiple times using the index.
        # if we've found the lowest price, we can't ALSO be finding the max_profit. So skip it.
        # 99.55, 10.57
        lowest = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < lowest:
                lowest = price
            elif price - lowest > max_profit:
                max_profit = price - lowest
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        diff = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif price - lowest > diff:
                diff = price - lowest
        return diff
            