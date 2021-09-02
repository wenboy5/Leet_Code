'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        k,p=0,5
        while(n>=p):
            k,p=k+n//p,p*5
        return k   
'''
Here the condition is when the factorial traverses through 5*n and its multiples like 5,25,75,625,... one extra zero will be for each 5 multiple. For example, when factorial contains 5 in between one zero is added, for 15 it is divisible only once by 5 so one zero is added, for 25 it is divisible by 5 twice so two zeros are added, for 125 it is divisible by 5 three times so three zeros are added, so in the loop for all 5 divisible numbers we add one zero and the second loop for all 25 divisible numbers we add extra zeros,... and the loop continues
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        dp =[[i,0] for i in range(n+1)]
        dp[0][0] = 1
        #print(dp)
        
        for i in range(1,n+1):
            dp[i][0] = str(dp[i][0] * dp[i-1][0])
            dp[i][1] = dp[i-1][1]
            
            while dp[i][0][-1] == "0":
                dp[i][0] = dp[i][0][:-1]
                dp[i][1] += 1
            if len(dp[i][0]) > 5:
                dp[i][0] = int(dp[i][0][-5:])
            else:
                dp[i][0] = int(dp[i][0])
        #print(dp)
        return dp[-1][1]

#time limit exceeded
class Solution:
    def trailingZeroes(self, n: int) -> int:
        dp =[i for i in range(n+1)]

        dp[0] = 1
        
        for i in range(1,n+1):
            dp[i] = dp[i] * dp[i-1]
        return len(str(dp[-1])) - len(str(int(str(dp[-1])[::-1])))
    