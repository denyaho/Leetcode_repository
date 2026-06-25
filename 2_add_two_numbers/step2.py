
#他の人のコードを参照
# https://github.com/MA-yo-TA/leetcode/blob/2-Add-Two-Numbers/2_Add_Two_Numbers/step2.py
# https://github.com/atmaxstar/coding_practice/blob/2/2.%20Add%20Two%20Numbers/memo.md


#自分なりに以下のように書き換え

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        carry = 0
        node = sum_list
        while l1 or l2 or carry:
            sum_val = 0
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            sum_val += carry
            carry = sum_val // 10
            node.next = ListNode(sum_val % 10)
            node = node.next
        return sum_list.next