# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst1 = []
        lst2 = []
        while l1.next != None:
            lst1.append(l1.val)
            l1 = l1.next
        lst1.append(l1.val)
        
        while l2.next != None:
            lst2.append(l2.val)
            l2 = l2.next
        lst2.append(l2.val)

        x = len(lst1)
        y = len(lst2)
        
        num1 = 0
        num2 = 0      
        for i in range(x):
            num1 += (10 ** (x-i-1)) * lst1[-i-1]
        for i in range(y):
            num2 += (10 ** (y-i-1)) * lst2[-i-1]
        sum = num1 + num2

        res = ListNode()
        head = res
        strsum = str(sum)
        head.val = strsum[-1]
        for i in range(len(strsum)-1):
            newNode = ListNode(strsum[-i-2])
            head.next = newNode
            head = head.next
        
        return res