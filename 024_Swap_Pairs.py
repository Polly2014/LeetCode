# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-17 23:39:03
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-17 23:47:37
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 递归(时间、空间复杂度均为O(N))
    def swapPairs(self, head: ListNode) -> ListNode:
        # 没有或只有一个节点时，直接返回（即是边界也是起始判断）
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

    # 迭代
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next
