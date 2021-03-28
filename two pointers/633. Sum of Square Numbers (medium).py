"""Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true
"""
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = math.floor(math.sqrt(c))
        lst = [i ** 2 for i in range(x+1)]
#        for i in lst:
#            print(i)
        lo,hi = 0, len(lst)-1
        while lo<=hi:
            if lst[lo] + lst[hi] > c:
                hi-=1
            elif lst[lo] + lst[hi] < c:
                lo+=1
            else:
                return True
        return False

#还是前面的更快
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = math.floor(math.sqrt(c))
#        lst = [i ** 2 for i in range(x+1)]
#        for i in lst:
#            print(i)
#        print(len(lst)-1 == x)
        lo,hi = 0, x
        while lo<=hi:
            if lo ** 2 + hi ** 2 > c:
                hi-=1
            elif lo ** 2 + hi ** 2 < c:
                lo+=1
            else:
                return True
        return False