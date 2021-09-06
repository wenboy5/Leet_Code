'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def compare(self,root,head):
    #     if root.val == head.val and not root.left and not root.right and not head.right and not head.left:
    #         return True
    #     elif root.left and head.left and root.right and head.right:
    #         return  root.val == head.val and self.compare(root.left,head.left) and self.compare(root.right,head.right)
    #     elif root.left and head.left:
    #         return root.val == head.val and self.compare(root.left,head.left)
    #     elif root.right and head.right:
    #         return root.val == head.val and self.compare(root.right,head.right)
    #     else:
    #         return False
    
    def compare(self, root, head):
        if not root and not head:
            return True
        if root and head:
            return root.val == head.val and self.compare(root.left, head.left) and self.compare(root.right, head.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, head):
            if root.val == head.val and self.compare(root,head):
                return True
            elif root.left or root.right:
                a = b = False
                if root.left:
                    a = check(root.left,head)
                if root.right:
                    b = check(root.right,head)
                return a or b
            else:
                return False
        return check(root,subRoot)