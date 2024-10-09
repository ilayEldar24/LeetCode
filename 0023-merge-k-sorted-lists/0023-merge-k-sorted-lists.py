
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeLists(l1, l2):
    dummy = ListNode(-1)
    cur = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = ListNode(l1.val)
            l1 = l1.next
        else:
            cur.next = ListNode(l2.val)
            l2 = l2.next
        cur = cur.next
    
    while l1:
        cur.next = ListNode(l1.val)
        l1 = l1.next
        cur = cur.next
    while l2:
        cur.next = ListNode(l2.val)
        l2 = l2.next
        cur = cur.next
    
    return dummy.next
        
           
class Solution(object):
    def mergeKLists(self, lists):
        def helper(lists, s, e):
            if not lists:
                return None
            if s > e:   
                return None
            
            if s == e:
                return lists[s]
            
            m = (s+e) // 2
            left = helper(lists, s, m)
            right = helper(lists, m+1, e)
            return mergeLists(left, right)
        
        s = 0
        e = len(lists) - 1
        return helper(lists,s,e)

