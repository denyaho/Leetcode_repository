#Runtime 54ms
#Memory 22.43MB

#Time complexity O(N)
#Space complexity O(1)

# #解法
# この解放は、Floyd法を利用し、1ステップずつ進むslowと、2ステップずつ進むfastを用いて、Linked listにサイクルがあるかどうかを検知する。
# サイクルがなければ、Noneを返し、サイクルがあれば、サイクルが始まる開始ノードを見つける。

# 開始ノードを見つけるための方法は以下の考え方。

# 変数
# a-> headからサイクルの開始ノードまでの距離
# b-> サイクルの開始ノードから、slowとfastが出会うノード
# c-> サイクルの開始ノードから、サイクルの終わりまでの距離

# slowは１ステップずつ、fastは2ステップずつ進む。
# slowとfastが出会うために、slowはa+bの距離を進み、fastはa+b+c*kの距離を進む必要がある。(kはサイクルの周回数)

# お互い、進んだ距離は同じため、2(a+b) = a+b+c*kが成り立つ。
# この式を変形すると、a = c*k - bとなる。

# で、次に、headの位置から再度1ステップずつ進む変数from_startと、
# slowとfastが出会った位置から進む変数from_pointを用意する。

# この二つの変数は同じ距離を進むため、from_startがサイクルの開始ノードまでの距離(a)を進むと、
# from_pointは現在地点からc*k - bの距離を進むことになる。

# bの位置からc*k - b距離を進むことをわかりやすくすると、
# (b - b) + c*kとなる。
# これはサイクルの開始ノードに到達し、さらにc*kでサイクルをk周することになる。
# つまり、from_startとfrom_pointは同時にサイクルの開始ノードに到達することになる。

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


##自分は最初溶けなかったので、他の人のコードを参考にしました。
#　自分の回答はstep3.pyに記載しています。
# https://github.com/MA-yo-TA/leetcode/blob/142-linked-list-cycle-ii/142_Linked_List_Cylce_II/step1_floyd.py



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # まず fast と slow が出会う点を見つける
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                break

        else:
            return None

        # fast と slow が合流したなら、片方をスタート地点に戻して同じ速さで再度歩かせると次に合流する点がサイクルの始まりの点
        slow = head

        while True:
            if fast is slow:
                return fast

            fast = fast.next
            slow = slow.next