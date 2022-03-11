'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        squared_distance= lambda x, y : x*x + y*y
        for p in points:
            p.insert(0, squared_distance(p[0], p[1]))
        heapify(points)
        return [heappop(points)[1:] for i in range(k)]
      
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for x,y in points:
            dis = (x**2 +y**2)**(1/2)
            bisect.insort(l,(dis,[x,y]))
            if len(l) > k:
                l.pop()
        return [i[1] for i in l[:k]]
      
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for x,y in points:
            dis = (x**2 +y**2)**(1/2)
            bisect.insort(l,(dis,[x,y]))
        return [i[1] for i in l[:k]]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        for x,y in points:
            dis = (x**2 +y**2)**(1/2)
            l.append((dis,[x,y]))
        l.sort()
        return [i[1] for i in l[:k]]