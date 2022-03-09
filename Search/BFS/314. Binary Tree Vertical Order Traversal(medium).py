'''
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        if root == None:
            return []
        def traversal(root):
            stack = [root]
            root.level = 0
            while stack:
                temp = stack.pop(0)
                d[temp.level].append(temp.val)
                if temp.left:
                    temp.left.level = temp.level-1
                    stack.append(temp.left)
                if temp.right:
                    temp.right.level = temp.level+1
                    stack.append(temp.right)
        traversal(root)
        ans = []
        print(d)
        for i in sorted(d.items()):
            ans.append(i[1])
        return ans