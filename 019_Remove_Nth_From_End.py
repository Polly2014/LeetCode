# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-23 22:00:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-23 22:15:18

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast, slow = head, dummy
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        else:
            slow.next = slow.next.next
        return dummy.next
