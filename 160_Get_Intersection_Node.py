# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-07 21:45:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-07 21:48:13
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
