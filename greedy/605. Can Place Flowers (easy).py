'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

#think of edge cases
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed.count(0)< 2*n-1:
            return False
        
        res = 0   
        l0 = len(flowerbed)
        if l0 == 0:
            return 0 == n
        elif l0 == 1:
            return 1-flowerbed[0] >= n
        elif l0 == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                return 1 >= n
            else:
                return 0 == n
            
        l1 = len(flowerbed[:-2])
        i = 0
        while(i<l1):
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        res+=1
                    i+=2        
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        res += 1
                        i += 2
                    elif flowerbed[i+1] == 0:
                        i+=1
                    else:
                        i +=2
        if flowerbed[-1] ==0 and flowerbed[-2] == 0:
            res += 1
        return res >= n