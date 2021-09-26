# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-25 17:28:18
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-25 17:33:32
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smallHead = ListNode(0)
        bigHead = ListNode(0)
        smallTail = smallHead
        bigTtail = bigHead
        while head:
            if head.val < x:
                smallTail.next = head
                smallTail = smallTail.next
            else:
                bigTtail.next = head
                bigTtail = bigTtail.next
            head = head.next
        # 将大小链表拼合在一起
        smallTail.next = bigHead.next
        bigTtail.next = None
        return smallHead.next
