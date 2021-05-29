'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp =[]
        count = 0
        flag = True
        while head != None:
            count+=1
            temp.append(head)
            head = head.next
            if count == k:
                #print(temp)
                count = 0
                if flag:
                    flag = False
                    res = temp[-1]
                    ans = res
                    #print("here")
                    temp = temp[:k-1]
                    for i in temp[::-1]:
                        #print("**")
                        #print(i.val)
                        res.next = i
                        res = res.next
                else:
                    for i in temp[::-1]:
                        res.next = i
                        res = res.next
                temp = []         
                
        if temp != []:
            for i in temp:
                res.next = i
                res = res.next
        else:
            res.next = None
                        
                    
        return ans