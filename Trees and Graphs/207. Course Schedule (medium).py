'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    
    class GraphNode:
        def __init__(self):
            self.out = []  
            self.state = 0
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: self.GraphNode() for i in range(numCourses)}
        
        for p in prerequisites:
            src = p[0]
            dest = p[1]
            graph[src].out.append(dest)
        
        def dfs(currCourse):
            if (graph[currCourse].state == 1): 
                return True
            if graph[currCourse].state == 2: 
                return False
            
            graph[currCourse].state = 1
            
            for i in graph[currCourse].out:
             
                if dfs(i):
                    return True
            
            graph[currCourse].state = 2
            
            return False
            
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        
    