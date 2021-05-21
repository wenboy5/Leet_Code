'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i == "(" or i=="[" or i =="{":
                stack.append(i)
            elif i == ")":
                if len(stack) >= 1 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            elif i == "}":
                if len(stack) >= 1 and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            elif i == "]":
                if len(stack) >= 1 and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        if stack == []:
            return True
        else:
            return False