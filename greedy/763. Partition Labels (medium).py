'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        i = left = right = 0
        inverse = S[::-1]
        res = []
        while i < len(S):
            
            right = max(right,len(S)-1-inverse.index(S[i]))
     
            if i == right:
                res.append(right - left + 1)
                left = i + 1
            i += 1
        return res