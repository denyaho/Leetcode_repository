## Runtime 0ms
# Memory 19.26MB

#時間計算量 O(n)
#空間計算量 O(1)


#自分なりにわかりやすくしたコード

#書き方１
# このコードはnextが多すぎてちょっと追いにくくなっているのかなと思った

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        distinct_linked_list = dummy
        node = head
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                distinct_linked_list.next = node.next
            else:
                distinct_linked_list = distinct_linked_list.next
            node = node.next
        return dummy.next


#書き方２
#dummyでnextを初期化していて、一行で書いているのはわかりやすいと思う
#また、nextは１と比べて少ないので、追いやすいと思う

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        distinct_linked_list = dummy

        node = head
        while node and node.next:
            if node.val == node.next.val:
                current_val = node.val
                while node and node.val == current_val:
                    node = node.next
                distinct_linked_list.next = node 
                continue
            distinct_linked_list = distinct_linked_list.next
            node = node.next
        return dummy.next