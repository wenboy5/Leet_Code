'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num % 10 not in [1,4,5,6,9,0]:
            return False
        for i in range(1, int(num/2)+2):
            if i * i == num:
                return True
            elif i * i > num:
                return False
        