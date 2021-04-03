'''Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

 

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 

Constraints:

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s and dictionary[i] consist of lowercase English letters.
'''
from collections import defaultdict
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        d = defaultdict(list)
        
        def check(s1:str, s2:str)->bool:
            p1,p2=0,0
            if len(s1) == 0 or len(s2) == 0:
                return False
            while(p1<len(s1)):
                if s1[p1] == s2[p2]:
                    p2+=1
                p1+=1
                if p2 == len(s2):
                    return True
            return False
            
        for each in dictionary:
            if check(s,each):
                d[len(each)].append(each)
                
        if d == {}:
            return ""
        longest = max(d.keys())
        if len(d[longest]) == 1:
            return d[longest][0]
        else:
            return min(d[longest])

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            idx = 0
            for ch in word:
                idx = s.find(ch, idx) + 1
                if not idx: break
            else: return word
        return ''