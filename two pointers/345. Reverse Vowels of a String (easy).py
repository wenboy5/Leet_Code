'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def is_vowels(self, s:str) -> bool:
        return True if s in ('a','e','i','o','u','A','E','I','O','U') else False
    
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        lo,hi = 0,len(lst)-1
        while lo<hi:
            if self.is_vowels(lst[lo]) and self.is_vowels(lst[hi]):
                lst[lo],lst[hi]=lst[hi],lst[lo]
                lo+=1
                hi-=1
            elif not self.is_vowels(lst[lo]):
                lo+=1
            elif not self.is_vowels(lst[hi]):
                hi-=1
        return "".join(lst)
          
#use list.pop() 同时还可以 +

class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for i in s:
            if i in 'aeiouAEIOU':
                stack.append(i)
        res = ""
        for i in s:
            if i in 'aeiouAEIOU':
                res += stack.pop()
            else:
                res += i
        return res