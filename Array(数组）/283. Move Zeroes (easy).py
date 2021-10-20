'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i in nums:
            if i != 0:
                nums[lastNonZeroFoundAt] = i
                lastNonZeroFoundAt += 1
        
        for i in range(lastNonZeroFoundAt,len(nums)):
            nums[i] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        other = []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                other.append(i)
        new = other + zero
        for i in range(len(nums)):
            nums[i] = new[i]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if nums[i] == 0:
                for j in range(i+1,len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] =nums[j], nums[i]
                        break
        

class Solution:
    def moveZeroes(self, nums):
        nums.sort(key=lambda i: i==0) #returns False (0) if not zero and True (1) if zero. Hence zero follows non-zero numbers


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:   #check if the number is zero (if yes)
                nums.append(0) #add zero to the end of the list
                nums.remove(0) #remove the first zero found (from left)