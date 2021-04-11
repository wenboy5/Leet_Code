'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-2 * 104 <= starti < endi <= 2 * 104
'''

#time limit exceeded
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        print(intervals)
        
        def recursion(intervals):
            if (len(intervals) == 0):
                return 0
            elif (len(intervals) == 1):
                return 1
            else:
                for i in range(1,len(intervals)):
                    if (intervals[0][1]<=intervals[i][0]):
                        break
                else: return max(recursion([])+1,recursion(intervals[1:]))
                return max((recursion(intervals[i:]) + 1), recursion(intervals[1:]))
        
        return len(intervals) - recursion(intervals)


#slow
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = [1] * len(intervals)
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if( intervals[i][1]<= intervals[j][0] ):
                    l[j] = max(max(l[:i+1])+1,l[j])
                    break
        return len(intervals) - max(l)



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        
        intervals.sort(key=lambda e: e[1])
        
        count = 0
        stack = [intervals[0]]
        
        for i in range(1, n):
            interval = intervals[i]
            if len(stack) > 0 and interval[0] < stack[-1][1]:
                count += 1
            else:
                stack.append(interval)
                
        return count