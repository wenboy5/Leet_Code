'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        l = []
        while head != None:
            l.append(head)
            head = head.next
        head = l[-1]
        for i in reversed(range(1,len(l))):
            l[i].next = l[i-1]
        l[0].next = None
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l = []
        while head != None:
            l.append(ListNode(head.val))
            head = head.next
        
        if len(l) == 0:
            return None
    
        l = [None] + l 
        ans = l[-1]
        for i in reversed(range(1,len(l))):
            l[i].next = l[i-1]
        return ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l = []
        while head != None:
            l.append(ListNode(head.val))
            head = head.next
        
        if len(l) == 0:
            return None
        elif len(l) == 1:
            return l[0]
        
        l = l[::-1] +[None]
        flag = True
        for i in range(len(l)-1):
            print(i)
            if flag:
                head = l[i]
                ans = l[i]
                flag = False
            else:   
                head.next = l[i]
                head = head.next
        return ans