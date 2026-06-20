# 206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/description/

## step1

まず考えたことは、リストを用意してノードの要素を全てappendで入れていき、一番後ろからpopで取り出していく形式だが、
O(N)の空間計算量が必要になるので in-place で実行できるアルゴリズムが必要になった。

逆順ということは、現在のnodeのnextポインタが一個前のnodeを示すようにすればいいので、prevという
変数を持っておき、現在のnodeのnextポインターがprevを示すようにする。
こうすると、nodeの探索ができなくなってしまうので、nextという変数を持ち、nodeのnextポインタを保持するようにする。

```

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
```

## step2（整形＆他の人のコードを読む）

他の人も同様なコードを利用していた
自分の場合はprevをreverse linked listとして使用したが、変数がよくわからなかったと思う。
prevはcurの一個前の要素なので、名前を変えるかもう一つreverse linked listを示す変数を持っても良かったと思う

参考PR

https://github.com/MA-yo-TA/leetcode/pull/8/changes
https://github.com/wanwan87/LeetCode_arai60/pull/7/changes
https://github.com/enari-k/LeetCode/pull/64/changes
https://github.com/tamagoyaki-chiu/LeetCode-Practice/pull/12


参照したPRの中には再帰のことを言及しているPRもあった。
再帰が苦手で、あんまりイメージが湧かないのでちゃんと読み、書けるようにする


以下の再帰では、
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
```

