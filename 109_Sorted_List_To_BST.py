# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 21:17:22
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 21:25:31
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left, right):
            if left == right:
                return
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        return buildTree(head, None)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def builtTree(A):
            n = len(A)
            if n == 0:
                return None
            m = (n - 1) // 2
            root = TreeNode(A[m])
            root.left = builtTree(A[:m])
            root.right = builtTree(A[m + 1:])
            return root
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        return builtTree(val_list[:])
