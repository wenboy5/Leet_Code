# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None and l2 == None:
            return None
        elif l1 == None and l2 != None:
            res = ListNode(l2.val)
            l2 = l2.next
        elif l2 == None and l1 != None:
            res = ListNode(l1.val)
            l1 = l1.next
        else:
            if l1.val < l2.val:
                res = ListNode(l1.val)
                l1 = l1.next
            else:
                res = ListNode(l2.val)
                l2 = l2.next
        
        ans = res
        
        while l1!=None or l2!=None:
            if l1!= None and l2!=None:
                if l1.val < l2.val:
                    temp = ListNode(l1.val)
                    res.next = temp
                    res = res.next
                    l1 = l1.next
                else:
                    temp = ListNode(l2.val)
                    res.next = temp
                    res = res.next
                    l2 = l2.next
            elif l1 != None:
                temp = ListNode(l1.val)
                res.next = temp
                res = res.next
                l1 = l1.next
            elif l2 != None:
                temp = ListNode(l2.val)
                res.next = temp
                res = res.next
                l2 = l2.next
        return ans