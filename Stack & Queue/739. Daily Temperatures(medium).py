'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing stack
        stack = []
        n = len(temperatures)
        res = [0] * n
        
        for i in range(n):
            t = temperatures[i]
            while stack != [] and temperatures[stack[-1]] < t:
                less_index = stack.pop()
                res[less_index] = i - less_index
            stack.append(i)
        return res


# time limit exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[i] < temperatures[j]:
                    ans.append(j-i)
                    break
            else:
                ans.append(0)
                
       
        return ans