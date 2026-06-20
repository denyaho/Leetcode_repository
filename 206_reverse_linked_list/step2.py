from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None
        node = head
        while node is not None:
            next_node = node.next
            node.next = reversed_head
            reversed_head = node
            node = next_node

        return reversed_head