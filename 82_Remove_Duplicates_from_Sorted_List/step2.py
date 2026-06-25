##ここでは、他の人の書いたコードを参照して、どういったことをしているのかを学ぶ

# 参照先
# https://github.com/MA-yo-TA/leetcode/blob/82-Remove-Duplicates-from-Sorted-List-II/82_Rmove_Duplicates_from_Sorted_List_II/step2.py


# #解析
# このコードは、headという単方向の連結リストから重複を消して新たな連結リストを作成する。
# そのため、headの場所が変わる可能性がある。
# よって、headの前にdummy_headというノードを作成して、そこから連結リストを構築していく。

# 重複を探す際は、重複があるところからwhileループを回して重複がなくなるまでnode.nextを更新していく。
# 最終的には、重複があるノードの次の候補をnode.nextとして保存。

# その後、重複がない場合はnode = node.nextで移動していく


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=float("-inf"), next=head)
        node = dummy_head
        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                duplicate_value = node.next.val
                while node.next and node.next.val == duplicate_value:
                    node.next = node.next.next
            else:
                node = node.next

        return dummy_head.next
    
