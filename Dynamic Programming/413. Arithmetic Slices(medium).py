'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        new = [0] * (n-1)
        for i in range(n-1):
            new[i] = nums[i+1] -nums[i]
        print(new)
        cnt = 0
        for i in range(n-2):
            j = i
            print(j)
            while (new[j] == new[j+1]):
                cnt+=1
                j+=1
                if j == n-2:
                    break
        return cnt


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        le=len(A)
        l=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i]=1+l[i-1]
        return sum(l)