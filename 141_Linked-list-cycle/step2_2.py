## 概要
# Floyd の循環検出法を用いる

##アルゴリズム
# 早く動くポインタ(2ステップずつ)と、遅く動くポインタ(1ステップずつ)を用意する。
#これを同時に動かし、以下のような条件を確認する。

# 循環がある場合-> 早く動くポインタと遅く動くポインタが同じ場所にいることがある
# 循環がない場合-> 早く動くポインタが連結リストの終わりに到達する

##時間計算量 O(N)
##空間計算量 O(1)

#runtime 42ms
#memory 22.27MB


from typing import Optional
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True




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