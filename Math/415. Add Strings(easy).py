'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        add = 0
        ans = ""
        less, more = (num1,num2) if len(num1) <len(num2) else (num2,num1)
        less = "0"*(len(more)-len(less))+ less
        for i in range(-1,-len(more)-1,-1):
            total = int(less[i]) + int(more[i]) + add
            if total >= 10:
                ans = str(total-10) + ans
                add = 1
            else:
                ans = str(total) + ans
                add = 0
        if add == 1:
            ans = "1" + ans
        return ans