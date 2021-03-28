#brute force time O(n2) space O(1)
'''
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst_len = len(numbers)
        for i in range(lst_len):
            first_num = numbers[i]
            first_index = i + 1
            for j in range(first_index, lst_len):
                print(j)
                sec_num = numbers[j]
                sec_index = j + 1
                if ((first_num + sec_num) == target):
                    return [first_index, sec_index]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for count,value in enumerate(numbers):
            if target-value in numbers:
                first_index = count+1
                left = target-value
                break
        for i in range(len(numbers)):
            if left == numbers[i]:
                sec_index = i+1
        return [first_index, sec_index]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while True:
            sum = numbers[lo] + numbers[hi]
            if sum < target:
                lo+=1
            elif sum > target:
                hi-=1
            else:
                return [lo+1,hi+1]