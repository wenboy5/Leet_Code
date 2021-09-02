'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
'''
# !use median not avg
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        nums.sort()
        
        
     
        std = nums[int(len(nums)/2)]
        
        nums.remove(std)
        
        return sum(abs(i-std) for i in nums)