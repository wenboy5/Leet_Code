'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2

'''

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        flag = True
        for val in collections.Counter(s).values():
            if flag and val % 2 == 1:
                ans += val
                flag = False
            elif val % 2 == 1:
                ans += (val-1)
            else:
                ans += val
        return ans

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        
        for i in s:
            d[i] += 1
        ans = 0
        if len(d.values()) == 1:
            return sum(d.values())
        flag = True
        for val in d.values():
            if flag and val % 2 == 1:
                ans += val
                flag = False
            elif val % 2 == 1:
                ans += (val-1)
            else:
                ans += val
        return ans