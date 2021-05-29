'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

            def is_mirror(node1, node2) -> bool:
                if not node1 and not node2:
                    return True            
                if not node1 or not node2:
                    return False
                return node1.val == node2.val and \
                        is_mirror(node1.left, node2.right) and \
                        is_mirror(node1.right, node2.left)

            return is_mirror(root.left, root.right)
