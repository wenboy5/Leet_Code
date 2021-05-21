'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left =0
        right = len(height)-1
        left_max = 0
        right_max=0
        ans =0
        while left<right:
            if height[left] < height[right]:
                if height[left]>=left_max:
                    left_max = height[left]
                else:
                    ans+= (left_max-height[left])
                left = left +1
            else:
                if height[right]>=right_max:
                    right_max = height[right]
                else:
                    ans+= (right_max-height[right])
                right = right-1
        return ans


class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        res = 0
        while (start<end):
            if height[start] == 0:
                start += 1
            elif height[end] == 0:
                end -= 1
                
            low = min(height[start],height[end])
            
            for i in range(start+1,end):
                if height[i]<low:
                    res += low - height[i]
                    height[i] = low
                 
            print(height)
            if height[start] > height[end]:
                while height[start] > height[end]:
                    end -= 1
                    if height[end] > height[end+1]:
                        break
            elif height[start] < height[end]:
                while height[start] < height[end]:
                    start +=1
                    if height[start] > height[start-1]:
                        break
            else:
                while height[start] <= height[end]:
                    if start == end:
                        return res
                    start +=1
            
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        res = 0
        while (start<end):
            if height[start] == 0:
                start += 1
            elif height[end] == 0:
                end -= 1
                
            low = min(height[start],height[end])
            
            for i in range(start+1,end):
                if height[i]<low:
                    res += low - height[i]
                    height[i] = low
                 
            
            if height[start] > height[end]:
                end -= 1
            else:
                start +=1
        return res