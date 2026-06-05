#他の人のコードも参考に、自分なりに修正したコード

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        has_Cycle = False
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                has_Cycle=True
                break
        if not has_Cycle:
            return None

        from_start = head
        from_point = fast

        while from_start is not from_point:
            from_start = from_start.next
            from_point = from_point.next
        
        return from_start
            