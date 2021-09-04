'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        check =set()
        l = []
        while head!= None:
            if head.val not in check:
                check.add(head.val)
                l.append(ListNode(head.val))
            head = head.next
        l.sort(key = lambda x : x.val)
        l = l + [None]
        ans = l[0]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return ans