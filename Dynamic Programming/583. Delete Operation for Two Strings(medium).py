'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n=len(word1)
        m=len(word2)
        
        dp=[ [0 for _ in range(m+1)] for _ in range(n+1) ]
        
        
        for i in range(1,m+1):
            dp[0][i] = i
        for j in range(1,n+1):
            dp[j][0] = j
        
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i][j-1] , dp[i-1][j])
                    
        return dp[n][m]