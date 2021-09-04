'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # dummy -> A -> B -> C 
        
        # we want to swap A and B so we have to make dummy to point towards B and B towards A and A towards C 
        
        
        # dummy >>>>> B
        # B >>>>> A
        # A >>>>> C 
        # all steps simultaneously
        dummy = ListNode(0)
        
        dummy.next = head
        
        start = dummy
        
        
        while dummy.next and dummy.next.next:
            
            temp1 = dummy.next # A
            temp2 = temp1.next # B
            
            dummy.next ,temp2.next , temp1.next = temp2 , temp1, temp2.next
            
            dummy = temp1
            
        return start.next
            
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        l = []
        while head != None:
            l.append(ListNode(head.val))
            head = head.next
        
        for i in range(0,len(l),2):
            if i+1 < len(l):
                l[i], l[i+1] = l[i+1], l[i]
                
        l = l + [None]
        ans = l[0]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        return ans

