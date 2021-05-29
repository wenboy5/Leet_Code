'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        l = [root]
        res = []
        while l:
            temp = []
            for i in range(len(l)):
                first = l.pop(0)
                temp.append(first.val)
                left = first.left
                right = first.right
                if left:
                    l.append(left)
                if right:
                    l.append(right)
            res.append(temp)
        return res