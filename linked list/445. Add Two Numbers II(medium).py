'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        n2 = []
        while l1 != None:
            n1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            n2.append(l2.val)
            l2 = l2.next
        less, more = (n1, n2) if len(n1) <= len(n2) else (n2, n1)
        less = [0] * (len(more) - len(less)) + less
        

        add = 0
        for i in reversed(range(len(more))):
            more[i] = more[i] + less[i] + add
            if more[i] >= 10:
                add = 1
                more[i] -= 10
            else:
                add = 0
        if add == 1:
            more = [1] + more 
        for i in range(len(more)):
            more[i] = ListNode(more[i])
        ans = more[0]
        more = more + [None]
        for i in range(len(more)-1):
            more[i].next = more[i+1]
        return ans