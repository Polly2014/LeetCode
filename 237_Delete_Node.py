# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-02 22:43:43
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-02 22:46:37
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
