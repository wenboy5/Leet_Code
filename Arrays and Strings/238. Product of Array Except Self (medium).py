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
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left = [1]*n
        right =[1]*n
        res = [1]*n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        
    
        for i in range(1,n):
            right[-i-1] = right[-i] * nums[-i]
        
        print(left)
        print(right)
        
        for i in range(n):
            res[i] = left[i]*right[i]
        return res

# too slow
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        left = [1]
        right =[1]
        num = 1
        for i in range(n-1):
            num = num*nums[i]
            left.append(num)
        
        num = 1
        nums = nums[::-1]
        for i in range(n-1):
            num = num*nums[i]
            right.insert(0,num)
        
        print(left)
        print(right)
        
        for i in range(n):
            res.append(left[i]*right[i])
        return res