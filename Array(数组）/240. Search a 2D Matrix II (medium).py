'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
'''
#O(log(n!)) O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def re(matrix):
            if matrix == []:
                return False
            flag = True
            for i in matrix:
                if i != []:
                    flag = False
                    break
            if flag:
                return False
            
            m = len(matrix)
            n = len(matrix[0])

            l = min(m,n)
            upper = 0
            for i in range(l):
                if matrix[i][i] == target:
                    return True
                elif matrix[i][i] > target:
                    upper = i
                    break
            if len(matrix)>= 1 and len(matrix[0]) >= 1 and target < matrix[0][0]:
                return False
            if upper == 0:
                return re([i[l:] for i in matrix]) or re(matrix[l:])
            else:
                return re([i[upper:] for i in matrix[:upper]]) or re([i[:upper] for i in matrix[upper:]])
        return re(matrix)


# O(mn) O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        
        return False

#O(nlogn) Space complexity : \mathcal{O}(\log n)O(logn)

# Although this approach does not fundamentally require greater-than-constant addition memory, its use of recursion means that it will use memory proportional to the height of its recursion tree. Because this approach discards half of matrix on each level of recursion (and makes two recursive calls), the height of the tree is bounded by \log nlogn.

# run binary search on the rows, for each row, and time complexity is still O(n log n)

#Search Space Reduction
#O(m+n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False