'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree(nums,root=None):
            if nums:
                mid = nums[int(len(nums)/2)]
                if not root:
                    root = TreeNode(mid)
                
                index = nums.index(mid)
                nums.remove(mid)
                root.left = create_tree(nums[:index])
                if index < len(nums):
                    root.right = create_tree(nums[index:])
                else:
                    root.right = create_tree([])

                return root
            else:
                return None
        return create_tree(nums)

        # def insert(root,n):
        #     while True:
        #         if n <root.val:
        #             if root.left:
        #                 root = root.left
        #             else:
        #                 root.left = TreeNode(n)
        #                 break
        #         else:
        #             if root.right:
        #                 root = root.right
        #             else:
        #                 root.right = TreeNode(n)
        #                 break
        
        