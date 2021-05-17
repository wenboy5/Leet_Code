'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        answer = set()
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                return answer
            start = i+1
            end = len(nums)-1
            res = 0- nums[i]
            while(start < end):
                if nums[start] + nums[end] == res:
                    answer.add((nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
                elif nums[start] + nums[end] < res:
                    start+=1
                else:
                    end-=1
        return [list(i) for i in answer]