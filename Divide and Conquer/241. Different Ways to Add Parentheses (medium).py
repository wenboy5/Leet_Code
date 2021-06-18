'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

def diffWaysToCompute(self, expression: str) -> List[int]:
    memo = {}
        
    def dfs(s: str) -> List[int]:
        if s.isdigit():
            return [int(s)]
        
        if s in memo:
            return memo.get(s)
        
        res = []
        for i in range(len(s)):
            if s[i] in "+-*":
                left = dfs(s[0: i])
                right = dfs(s[i + 1:])
                
                for x in left:
                    for y in right:
                        res.append(eval(str(x) + s[i] + str(y)))
                        
        memo.update({s: res})
        return res
    
    return dfs(expression)