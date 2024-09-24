class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        
        # Loop should check that fast and fast.next are not None
        while fast and fast.next:
            slow = slow.next  # Slow pointer moves one step
            fast = fast.next.next  # Fast pointer moves two steps

            # Cycle detected if fast and slow pointers meet
            if fast == slow:
                return True
        
        return False  # No cycle if we exit the loop
