# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-02 21:52:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-02 21:57:47
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head
        i = 0
        while i < k:
            fast = fast.next
            i += 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
