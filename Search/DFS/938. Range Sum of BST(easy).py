'''
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if not root:
            return 0
        stack = [root]
        while stack:
            temp = stack.pop()
            if low <= temp.val <= high:
                ans += temp.val
            if low < temp.val and temp.left:
                stack.append(temp.left)
            if temp.val < high and temp.right:
                stack.append(temp.right)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if root:
                if low <= root.val <= high:
                    ans += root.val
                if root.val < high:
                    dfs(root.right)
                if low < root.val:
                    dfs(root.left)
            return ans
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l = []
        ans = 0
        if root:
            l.append(root.val)

        def dfs(root):
            if root.left:
                l.append(root.left.val)
                dfs(root.left)
            if root.right:
                l.append(root.right.val)
                dfs(root.right)
            return l
        l = dfs(root)
        
        for i in l:
            if i >= low and i<= high:
                ans += i
        return ans