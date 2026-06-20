
#Memory 20.49 MB

#時間計算量 O(n) - 反転するリストの長さに比例します。
#空間計算量 O(1) - 追加のスペースは定数

#解法
#prev、cur、nextの3つのポインタを使用してリストを反転させます。

# 1. prevをNoneに初期化
# 2. curをheadに初期化
# 3. curがNoneになるまでループ
#    a. nextにcur.nextを保存
#    b. cur.nextをprevに設定
#    c. prevをcurに更新
#    d. curをnextに更新
# 4. prevを返す


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev