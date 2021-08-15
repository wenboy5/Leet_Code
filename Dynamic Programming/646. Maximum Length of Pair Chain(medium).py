'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
'''
#too slow  O(n^2) O(n)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[0])
        print(pairs)
        
        n = len(pairs)
        if n == 1 or n == 0:
            return n
        
        dp = [1] * (n+1)
        
        dp[0] = 0
        for i in range(2,n+1):
            for j in range(0,i-1):
                if pairs[j][1] < pairs[i-1][0]:
                    dp[i] = max(dp[i],dp[j+1]+1)
        return max(dp)
            
#O(n^2) O(n)
class Solution(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)


#Time Complexity:  O(NlogN) O(N)
class Solution(object):
    def findLongestChain(self, pairs):
        cur = float('-inf')
        #cur = -math.inf
        ans =  0
        for x, y in sorted(pairs, key = lambda x : x[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans

#