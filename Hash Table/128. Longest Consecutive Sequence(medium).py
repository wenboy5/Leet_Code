'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in nums:
                local = 1
                curr = i
                while curr + 1 in nums:
                    curr += 1
                    local += 1
                ans = max(ans,local)
        return ans


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(set(nums))
        ans = 1
        local = 1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]+1 == nums[i]:
                local += 1
            else:
                ans = max(ans,local)
                local = 1
        ans = max(ans,local)    
        return ans