###step1との差異は、visited_nodeをリストからセットに変更したこと
#セットを使うことで、in演算子の平均計算量がO(1)となる(ハッシュテーブルで管理しているため)ので、時間計算量がO(N)となる。

# Runtime 62ms
# Memory 23.10MB

# 時間計算量 O(N)
# while文のなかで、visited_node内に連結リストオブジェクトを格納している。これをif head in visited_nodeで確認しているため、visited_nodeの長さがNの時に、時間計算量がO(1)となる。whileで最悪N回のループをすることを考えると、空間計算量はO(N)となる。

# 空間計算量 O(N)

#実装方針
# step1の時と同様に、探索済みのノードを保存するためにセットを用いた

from typing import Optional
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        while head:
            if head in visited_node:
                return True
            visited_node.add(head)
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