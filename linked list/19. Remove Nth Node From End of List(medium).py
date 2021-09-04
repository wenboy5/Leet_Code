'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        l = []
        while head != None:
            l.append(ListNode(head.val))
            head = head.next
        a = len(l)
        l = l[:a-n] + l[a-n+1:] +[None]
        print(l)
        if len(l) == 1:
            return None
        ans = l[0]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return ans
        