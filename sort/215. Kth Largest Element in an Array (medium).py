'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
'''
# 时间复杂度 O(NlogK)，空间复杂度 O(K)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = sorted(nums[:k],reverse = True)
        for i in nums[k:]:
            if i > heap[-1]:
                heap.pop()
                heap.append(i)
                heap = sorted(heap,reverse =True)
        return heap[-1]

# 时间复杂度 O(NlogN)，空间复杂度 O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,reverse = True)
        return nums[k-1]

class Solution:
    def quickselect(self, left, right, nums, k):
        if left == right:       # If the list contains only one element,
          return nums[left]
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index= left
        for i in range(left, right):
            if nums[i]< pivot:
                nums[i],nums[store_index] = nums[store_index],nums[i]
                store_index += 1
        
        nums[right],nums[store_index]=nums[store_index],nums[right]
        
        if store_index == k:
            return nums[k]
        elif store_index < k:
            return self.quickselect(store_index+1,right,nums,k)
        elif store_index > k:
            return self.quickselect(left,store_index-1,nums,k)
        
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(0,len(nums)-1,nums,len(nums)-k)



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect( left, right, nums, k):
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)

            pivot = nums[pivot_index]

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store_index= left
            for i in range(left, right):
                if nums[i]< pivot:
                    nums[i],nums[store_index] = nums[store_index],nums[i]
                    store_index += 1

            nums[right],nums[store_index]=nums[store_index],nums[right]

            if store_index == k:
                return nums[k]
            elif store_index < k:
                return quickselect(store_index+1,right,nums,k)
            elif store_index > k:
                return quickselect(left,store_index-1,nums,k)

        return quickselect(0,len(nums)-1,nums,len(nums)-k)