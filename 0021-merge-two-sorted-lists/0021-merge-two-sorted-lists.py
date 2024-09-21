class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        res = dummy
        
        # Merge the two lists by adjusting pointers
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        
        # Append the remaining nodes from either list1 or list2
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        
        # Return the next node of dummy, which is the head of the merged list
        return dummy.next