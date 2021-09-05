'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        def dfs(root,total):
            if not root.left and not root.right and total == targetSum:
                return True
                
            elif root.left or root.right:
                a1 = a2 = False
                if root.right:
                    a1 = dfs(root.right,total+root.right.val)
                if root.left:
                    a2 = dfs(root.left,total+root.left.val)
                return a1 or a2
            else:
                return False
            
        return dfs(root,root.val)