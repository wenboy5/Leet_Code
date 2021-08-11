'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        f = [0] * n

        for i in range(n):
            max_lis = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_lis = max(max_lis, f[j])
            f[i] = max_lis + 1
        
        return max(f)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = []
        for i in range(len(nums)):
            if not f or nums[i] > f[-1]:
                f.append(nums[i])
            else:
                pos = bisect.bisect_left(f, nums[i])
                f[pos] = nums[i]
        return len(f)
