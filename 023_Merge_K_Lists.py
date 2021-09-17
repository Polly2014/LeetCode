# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-17 18:08:28
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 18:31:42
from typing import List
import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 优先队列解法
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

    # # 分治解法
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists:
    #         return None
    #     n = len(lists)
    #     return self.mergeLists(lists, 0, n - 1)

    # def mergeLists(self, lists, left, right):
    #     if left == right:
    #         return lists[left]
    #     mid = (left + right) // 2
    #     L1 = self.mergeLists(lists, left, mid)
    #     L2 = self.mergeLists(lists, mid + 1, right)
    #     return self.mergeTwoLists(L1, L2)

    # def mergeTwoLists(self, L1, L2):
    #     if not L1:
    #         return L2
    #     if not L2:
    #         return L1
    #     if L1.val < L2.val:
    #         L1.next = self.mergeTwoLists(L1.next, L2)
    #         return L1
    #     else:
    #         L2.next = self.mergeTwoLists(L1, L2.next)
    #         return L2
