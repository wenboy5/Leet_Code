'''
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last_index = 0
        for i in s:
            if last_index < len(t):
                if i not in t[last_index:]:
                    return False
                last_index = last_index + t[last_index:].index(i) +1
            else:
                return False
        
        return True
    
#two pointer
def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        i = 0
        while i < len(t) and c < len(s):
            if t[i] == s[c]:
                c += 1
            i += 1
        return c == len(s)