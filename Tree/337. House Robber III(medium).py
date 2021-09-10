'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''

class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        
        def helper(node, parent_stolen):
            if not node:
                return 0
            if parent_stolen:
                # we did steal from parent
                # the only option is to not steal since we stole from the parent
                return helper(node.left, False) + helper(node.right, False)
            else:
                # we did NOT steal parent
                # Given a choice to choose b/w stealing or not stealing
                # stealing at the current node
                steal = node.val + helper(node.left, True) + helper(node.right, True)
                # NOT stealing current node
                not_stealing = helper(node.left, False) + helper(node.right, False)
                
                return max(steal, not_stealing)
        
        return helper(root, False)

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))

