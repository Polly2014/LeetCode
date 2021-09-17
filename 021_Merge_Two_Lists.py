# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-17 16:46:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 16:50:40
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
