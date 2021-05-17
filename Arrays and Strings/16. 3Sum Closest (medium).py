'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = math.inf
        answer = 0
        print(answer)
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                temp = nums[start] + nums[end] + nums[i]
                print(temp)
                if abs(temp-target) < abs(diff):
                    diff = temp-target
                    answer = temp
                if temp - target == 0:
                    return target
                elif temp- target > 0:
                    end -= 1
                else:
                    start +=1
        return answer