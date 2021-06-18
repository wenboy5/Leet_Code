'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        return generate_trees(1, n) if n else []


def generateTrees(self, n: int) -> List[TreeNode]:
        def f(arr):
		    #Base conditions
            if len(arr) < 1:
                return [None]
            if len(arr) == 1:
                return [TreeNode(arr[0])]
            
            ret = []
            for i,item in enumerate(arr):
                leftTrees = f(arr[0:i])
                rightTrees = f(arr[i+1:])
                
                for lt in leftTrees:
                    for rt in rightTrees:
                        r = TreeNode(arr[i])
                        r.left = lt
                        r.right = rt
                        ret.append(r)
            return ret
        
        return f(list(range(1,n+1)))