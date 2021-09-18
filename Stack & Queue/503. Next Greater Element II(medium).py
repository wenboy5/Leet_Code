'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
'''


class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        result = [-1] * len(A)
        stack = []
        
        for pos, val in enumerate(A): 
            while stack and val > A[stack[-1]]:
                result[stack.pop()] = val   
            stack.append(pos)

        for pos, val in enumerate(A):  
            while stack and val > A[stack[-1]]:
                result[stack.pop()] = val

        return result
  
  
# very slow O(n^2)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_nums = nums + nums[:-1]
        ans = [-1] * n
        for i in range(len(nums)):
            item = nums[i]
            for j in range(i+1,i+n):
                if new_nums[j] > item:
                    ans[i] = new_nums[j]
                    break
        
        return ans