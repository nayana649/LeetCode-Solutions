class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Move fast pointer by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                
        # If the fast pointer reaches the end, no cycle exists
        return False