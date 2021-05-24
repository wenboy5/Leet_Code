"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        it = head
        cnt = 0
        while it != None:
            it.index = cnt 
            cnt+=1
            it= it.next
        
        order = [] #(val,index)
        while head!= None:
            if head.random == None:
                order.append((head.val,None))
            else:
                order.append((head.val,head.random.index))
            head = head.next
        print(order)
        
        
        
        newl = [0]*len(order)
        flag = True
        for i in range(len(order)):
            newl[i] = Node(order[i][0])
            
        for i in range(len(order)):
            if i == len(order)-1:
                newl[i].next = None
            else:
                newl[i].next = newl[i+1]
            if order[i][1] != None:
                print(order[i][1])
                newl[i].random = newl[order[i][1]]
            else:
                newl[i].random = None
        res = newl[0]
        return res