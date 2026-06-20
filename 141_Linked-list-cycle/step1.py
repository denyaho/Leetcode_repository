# Runtime 809ms
# Memory 22.62MB

# 時間計算量 O(N^2)
# while文のなかで、visited_node内に連結リストオブジェクトを格納している。これをif head in visited_nodeで確認しているため、visited_nodeの長さがNの時に、時間計算量がO(N)となる。whileで最悪N回のループをすることを考えると、空間計算量はO(N^2)となる。

#ちなみに、listの場合、in演算子は先頭から順に全探索するため平均計算量はO(N)、最悪計算量はO(N)となる。

# 空間計算量 O(N)

#実装方針
#  最初はvalのみをリストに保存しようと考えたが、値の重複があることを考えるとノードオブジェクトをリストに保存し、ノードオブジェクトの重複を確認する方法に変更した。


from typing import Optional
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = []
        while head:
            if head in visited_node:
                return True
            visited_node.append(head)
            head = head.next
        return False




###　以下はテストコードです。

if __name__ == "__main__":
    #テストケース１:
    start = time.time()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(Solution().hasCycle(node1))  # True
    print("time:", time.time() - start)

    #テストケース２:
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1
    print(Solution().hasCycle(node1))  # True

    #テストケース３:
    node1 = ListNode(1)
    print(Solution().hasCycle(node1))  # False