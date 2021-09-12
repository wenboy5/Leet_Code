'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = {}
        d[root] = None
    
        queue = [root]

        while (q not in d) or (p not in d):
            print("here")
            first = queue.pop(0)
            
            if first.right:
                print("right")
                d[first.right] = first
                queue.append(first.right)
            if first.left:
                print("left")
                d[first.left] = first
                queue.append(first.left)
        
        anc = set()
        while q:
            anc.add(q)
            q = d[q]
    
        
        while p not in anc:
            p = d[p]
        return p


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        q_l = p_l = []
        def find_path(root, l):
            nonlocal q_l, p_l
            if root:
                if root.val == p.val:
                    p_l = l + [root]
                if root.val == q.val:
                    q_l = l + [root]
                find_path(root.left,l+[root])
                find_path(root.right,l+[root])
           
        find_path(root,[])
        n = min(len(q_l),len(p_l))
        print(n)
        if n == 1:
            return q_l[0]
        else:
            for i in range(n):
                if p_l[i].val != q_l[i].val:
                    return p_l[i-1]
            return p_l[n-1]
                

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root,val):
            if root:
                if root.val == val:
                    return [root]
                else:
                    a = dfs(root.left,val)
                    b = dfs(root.right,val)
                    if a:
                        return [root] + a
                    elif b:
                        return [root] + b
                    else:
                        return []
            else:
                return []
            
        p_l = dfs(root,p.val)
        q_l = dfs(root,q.val)

        n = min(len(q_l),len(p_l))

        if n == 1:
            return q_l[0]
        else:
            for i in range(n):
                if p_l[i].val != q_l[i].val:
                    return p_l[i-1]
            return p_l[n-1]