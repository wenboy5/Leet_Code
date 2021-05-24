# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = [str(l1.val)]
        n2 = [str(l2.val)]
        
        while l1.next != None:
            l1 = l1.next
            n1.append(str(l1.val))
        while l2.next!= None:
            l2 = l2.next
            n2.append(str(l2.val))
            
        print(n1)
        print(n2)
        res = []
        total = int("".join(n1[::-1])) + int("".join(n2[::-1]))
        total = str(total)
        for i in reversed(range(len(total))):
            res.append(int(total[i]))
        head = ListNode(res[0])
        ans = head 
        for i in res[1:]:
            temp = ListNode(i)
            head.next= temp
            head = head.next
        return ans
            
            
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


#用到了recursion join reversed 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self,la:ListNode,lb=[]) -> list:
        lb.append(la.val)
        if la.next == None:
            return lb
        else:
            la = la.next
            return self.recursion(la, lb)
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst1 = self.recursion(l1,[])
        lst2 = self.recursion(l2,[])
        lst1 = reversed(lst1)
        lst2 = reversed(lst2)
        num1 = int("".join([str(i) for i in lst1]))
        num2 = int("".join([str(i) for i in lst2]))
        total = num1 + num2
        
        lst = list(reversed([i for i in str(total)]))
        res =ListNode(lst[0])
        res_ptr = res
        for i in lst:
            if i == lst[0]:
                continue
            new = ListNode(i)
            res_ptr.next = new
            res_ptr = res_ptr.next
        return res