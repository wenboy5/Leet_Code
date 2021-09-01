'''
iven an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 


59 ÷ 2 = 29 ... 1
29 ÷ 2 = 14 ... 1
14 ÷ 2 =  7 ... 0
 7 ÷ 2 =  3 ... 1
 3 ÷ 2 =  1 ... 1
 1 ÷ 2 =  0 ... 1
'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = False
        res = ""
        if num < 0:
            flag = True
            num = -num
        
        while num >=7:
            reminder = num%7
            res += str(reminder)
            num = num//7 #quotient
            
        res += str(num)
        
        if flag:
            res += "-"
        
        return res[::-1]