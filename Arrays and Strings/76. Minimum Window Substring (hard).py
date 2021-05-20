'''
Given two strings s and t of lengths m and n respectively, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of English letters.
'''

def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if not t or not s:
        return ""

    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1    

        # Keep expanding the window once we are done contracting.
        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    

# time limit exceeded
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return ""
        
        temp = set(t)
        left,right = 0,0
        
        end = len(s)-1
        answer=""
        answer_len = math.inf
        
        while left <= end and right <= end:
            if left < right:
                if len(temp) != 0:
                    if s[right] in temp:
                        temp.remove(s[right])
                        if (len(temp) == 0):
                            if right-left+1 < answer_len:
                                answer = s[left:right+1]
                        else:
                            right += 1
                else:
                    if s[left] in t:
                        temp.add(s[left])
                    left += 1 
                    if s[left] in temp:
                        temp.remove(s[left])
                        if (len(temp) == 0):
                            if right-left+1 < answer_len:
                                answer = s[left:right+1]
                    
            else:
                if s[left] in temp:
                    temp.remove(s[left])
                    right += 1
                else:
                    left += 1
                    right += 1
                