# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        head = ListNode()
        carry = 0
        cur = head

        #Define the first node
        if l1 and l2:
            head = ListNode((l1.val+l2.val) % 10)
            carry = (l1.val + l2.val) // 10
            l1 = l1.next
            l2 = l2.next
        elif l1:
            head = ListNode(l1.val)
            l1 = l1.next
        elif l2:
            head = ListNode(l2.val)
            l2 = l2.next
        else:
            return None
        

        cur = head

        while l1 and l2:
            cur.next = ListNode((l1.val+l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        while l1:
            cur.next = ListNode((l1.val + carry) %10)
            carry = (l1.val +  carry) // 10
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = ListNode((l2.val + carry) %10)
            carry = (l2.val +  carry) // 10
            l2 = l2.next
            cur = cur.next

        if carry:
            cur.next = ListNode(1)
    
        return head
        
