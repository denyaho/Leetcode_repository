

#Runtime 55ms
#Memory 22.68MB

#Time complexity O(N)
#space complexity O(N)

from typing import Optional



# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        isSeen = {}
        current_node = head
        while current_node:
            if current_node in isSeen:
                return current_node
            isSeen[current_node] = 0
            current_node = current_node.next
        return None