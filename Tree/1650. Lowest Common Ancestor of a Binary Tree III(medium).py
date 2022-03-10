'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

#         pt1, pt2 = p, q
        
#         while pt1 != pt2:
            
#             if pt1.parent == None: 
#                 pt1 = p
#             else:
#                 pt1 = pt1.parent
#             if pt2.parent == None: 
#                 pt2 = q
#             else:
#                 pt2 = pt2.parent
        
#         return pt1
        
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_path(node):
            p = [node]
            while node.parent != None:
                node = node.parent
                p.append(node)
            return p
        p_path = find_path(p)[::-1]
        q_path = find_path(q)[::-1]
        l = [i for i in p_path if i in q_path]

        return l[-1]
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root.parent != None:
            root=root.parent
        
        def dfs(root,target,l):
            if root:
                if root == target:
                    return l+[root]
                else:
                    return dfs(root.left,target,l+[root]) or dfs(root.right,target,l+[root])
                    
        p1 = dfs(root,p,[])
        p2 = dfs(root,q,[])
        
        path1 = [i.val for i in p1]
        path2 = [i.val for i in p2]

        n = min(len(path1),len(path2))

        for i in range(n):
            if path1[i] != path2[i]:
                return p1[i-1]

        return p1[n-1]