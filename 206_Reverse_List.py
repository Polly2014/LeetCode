# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-19 13:55:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-20 14:54:46
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归解法
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curr

    # 迭代解法
    def reverseList(self, head: ListNode) -> ListNode:
        # 穿针 pre,curr,next
        # 引线 curr.next->pre, pre->curr, curr->next
        p_pre = None
        p_curr = head
        while p_curr:
            p_next = p_curr.next
            p_curr.next = p_pre
            p_pre = p_curr
            p_curr = p_next
        return p_pre
