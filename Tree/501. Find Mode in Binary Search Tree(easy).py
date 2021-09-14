'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = collections.Counter()
        def re(root):
            if root:
                d[root.val] += 1
                re(root.left)
                re(root.right)
        re(root)
        ans = []
        a = max(val for val in d.values())
        
        for k,v in d.items():
            if v == a:
                ans.append(k)
        return ans

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # main variables
        mode = [root.val]
        freq_max = 1
        last = inf
        freq = 0
        
        # main function
        def in_order(node):
            nonlocal mode, freq_max, last, freq
            
            # call left node
            if node.left:
                in_order(node.left)
            
            # main operations
            if last == node.val:
                freq += 1
            
            else:
                if freq > freq_max:
                    freq_max, mode = freq, [last]
            
                elif freq == freq_max:
                    mode.append(last)
                    
                freq = 1
                last = node.val
            
            # call right node
            if node.right:
                in_order(node.right)
        
        # calling main function
        in_order(root)
        
        # edge cases
        if freq > freq_max:
            return [last]
        elif freq == freq_max:
                mode.append(last)
        print(mode)
        if freq_max == 1:
            return mode[1:]
        
        # default
        return mode