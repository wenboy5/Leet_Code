'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists == []:
            return None
        
        flag = True
        for i in lists:
            if i != None:
                flag = False
                break
        if flag:
            return None
        
        def merge(lists:List[ListNode]):
            if len(lists) >2:
                left = lists[:int((len(lists)/2))]
                right = lists[int((len(lists)/2)):]
                return merge([merge(left),merge(right)])
            else:
                if len(lists) ==1:
                    return lists[0]
                else:
                    l1 = lists[0]
                    l2 = lists[1]
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
        return merge(lists)
        