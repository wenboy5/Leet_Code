'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right






class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        ans = 0
        def dfs(root, total,l):
            nonlocal ans
            if total == targetSum:
                ans += 1
            if root.left or root.right:
                if root.left:
                    dfs(root.left,root.left.val+total,l+[root.left.val])
                if root.right:
                    dfs(root.right,root.right.val+total,l+[root.right.val])
        stack = [root]
        while stack:
            i = stack.pop()
            dfs(i,i.val,[i.val])
            if i.left:
                stack.append(i.left)
            if i.right:
                stack.append(i.right)
        return ans