# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        cur = head
        if head.next == None:
            return None
        for i in range(n):
            cur = cur.next
        
        l,r = head, cur
        
        if not r:
            return head.next
        
        while r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        
        return head
            
        
        
        
        
            
        