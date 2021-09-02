'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = 0
        ans = ""
        less, more = (a,b) if len(a) <len(b) else (b,a)
        less = "0"*(len(more)-len(less))+ less
        for i in range(-1,-len(more)-1,-1):
            total = int(less[i]) + int(more[i]) + add
            if total >= 2:
                ans = str(total-2) + ans
                add = 1
            else:
                ans = str(total) + ans
                add = 0
        if add == 1:
            ans = "1" + ans
        return ans

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = 0
        ans = ""
        less, more = (a,b) if len(a) <len(b) else (b,a)
        for i in range(-1,-len(less)-1,-1):
            total = int(less[i]) + int(more[i]) + add
            if total >= 2:
                ans = str(total-2) + ans
                add = 1
            else:
                ans = str(total) + ans
                add = 0
        for i in range(-len(less)-1,-len(more)-1,-1):
            total = int(more[i]) + add
            if total >= 2:
                ans = str(total-2) + ans
                add = 1
            else:
                ans = str(total) + ans
                add = 0
        if add == 1:
            ans = "1" + ans
        return ans