'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

class Solution(object):
    def partition(self, s):
        
        def isPalindrome(start, end):
            while start<end:
                if s[start] != s[end]:
                    return False
                else:
                    start+=1
                    end-=1
            return True
        
        ans = []
        def dfs(start,l):
            if start >= len(s):
                ans.append(l)
            for i in range(len(s) - start):
                if isPalindrome(start,start+i):
                    dfs(start+i+1, l+[s[start:start+i+1]])
        dfs(0,[])
        return ans