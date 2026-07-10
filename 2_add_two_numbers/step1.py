
#Runtime 0ms
#Memory 19.36MB

#時間計算量 O(n)
#空間計算量 O(1)

#考え方
#今回は二つのリストをのそれぞれの値を合計して、新たな連結リストを作成する必要がある。
#値の合計によっては、二つの連結リストよりも長い連結リストが必要になる可能性があるので、sum_listという新たな連結リストを用意した。
#carryという変数を用意して、足し算による繰り上がりがあった場合には記憶するようにした。

#足し合せでは、if条件文によりl1とl2の両方がある場合、l1だけがある場合、l2だけがある場合の３つのパターンを考慮している。
#それぞれのパターンで、carryを考慮して足し算をして、carryが発生した場合にはcarryを1にしている。
#最後にcarryが1のままになっている場合には、sum_listの最後に1を追加している。

#しかし、ちょっとコードが冗長になっているような気がするので、もう少し簡潔に書けるようにしたいと思う。

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_list = ListNode(0)
        node = sum_list
        list_val = 0
        while l1 or l2:
            if l1 and l2:
                if l1.val + l2.val + carry > 9:
                    list_val = l1.val + l2.val + carry - 10
                    carry = 1
                else:
                    list_val = l1.val + l2.val + carry
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l1 and l2 is None:
                if l1.val + carry > 9:
                    list_val = l1.val + carry - 10
                    carry = 1
                else:
                    list_val = l1.val + carry
                    carry = 0
                l1 = l1.next
            elif l2 and l1 is None:
                if l2.val + carry > 9:
                    list_val = l2.val + carry - 10
                    carry = 1
                else:
                    list_val = l2.val + carry
                    carry = 0
                l2 = l2.next
            node.next = ListNode(list_val)
            node = node.next
        if carry:
            node.next = ListNode(1)
        return sum_list.next
