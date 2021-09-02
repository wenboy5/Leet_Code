'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] + nums[:-1]
        right = nums[1:] + [1]
        #print(left,right)
        for i in range(1,n):
            left[i] = left[i] * left[i-1]
        #print(left)
        for j in range(-2,-n-1,-1):
            right[j] = right[j] * right[j+1]
        #print(right)
        
        return [right[i] * left[i] for i in range(n)]