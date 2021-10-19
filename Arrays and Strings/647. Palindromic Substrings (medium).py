'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        count = 0
        
        for l in range(0,len(s)):      # for different lengths l
            for i in range(len(s)-l):
                
                j=i+l
                
                if s[i]==s[j]: 
                    if i==j or i==j-1: #single and double letters
                        dp[i][j]=True                    
                    else:              #other cases
                        dp[i][j] = dp[i+1][j-1]
                    
                    count += dp[i][j]        # Increasing count if True           
        return count