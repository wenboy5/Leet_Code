'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for j in t:
            d[j] -= 1
        
        for val in d.values():
            if val != 0:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        a = s.copy()
        t = list(t)
        
        for i in a:
            print(i)
            if i not in t:
                print(i)
                return False
            else:
                s.remove(i)
                t.remove(i)
        print(t)
        return t == []