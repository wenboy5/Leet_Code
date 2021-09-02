'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""

        while columnNumber:
            re = columnNumber%26
       
            ans = s[re-1] + ans 
        
            if re == 0:
                columnNumber -= 1
            columnNumber =  columnNumber//26

            
        return ans