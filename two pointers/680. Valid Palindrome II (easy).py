'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 #initializing the left pointer to the beginning of the string
        r = len(s) - 1 #initializing the right pointer to the end of the string 
        
        while l <= r:
            if s[l] == s[r]: #if the string at both pointers is the same, move one step towards the center of the string
                l += 1
                r -= 1
            else: #incase the strings at each of the pointers aren't equal, ignore either of the characters and check if it is a palindrome
                return s[l:r][::-1] == s[l:r] or s[l + 1: r + 1][::-1] == s[l + 1:r + 1] 
        return True #the input string is a palindrome so we return True


def reverse_check(lo, hi, s, chance):
    if lo < hi:
        if s[lo] == s[hi]:
            return reverse_check(lo+1,hi-1,s,chance)
        elif s[lo] != s[hi] and s[lo] != s[hi-1] and s[lo+1] != s[hi]:
            return False
        elif s[lo] != s[hi] and chance >0:
            return reverse_check(lo+1,hi-2,s,chance-1) or reverse_check(lo+2,hi-1,s,chance-1)
        else:
            return False
    else:
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        chance = 1
        lst = list(s)
        lo, hi = 0, len(lst)-1
        return reverse_check(lo,hi,s,chance)


#recursion 速度太慢

def recheck(lo,hi,s):
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True
    

class Solution:
    def validPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s)-1
        while lo <hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                return recheck(lo+1,hi,s) or recheck(lo,hi-1,s)
        return True
        