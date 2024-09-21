# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        ptr1 = list1
        ptr2 = list2
        
        res = ListNode()
        dummy = res
         
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                res.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                res.next=ListNode(ptr2.val)
                ptr2 = ptr2.next
            res = res.next
            
        while ptr1:
            res.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            res = res.next
        
        while ptr2:
            res.next=ListNode(ptr2.val)
            ptr2 = ptr2.next
            res = res.next
        
        return dummy.next
    
            
        
                
                
                
        
        
        
        
        