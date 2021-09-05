# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-06 00:09:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-06 00:54:20
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = TreeNode(0)
        preOrderList = []

        def DFS(node):
            if not node:
                return
            preOrderList.append(node)
            DFS(node.left)
            DFS(node.right)
        DFS(root)
        n = len(preOrderList)
        for i in range(1, n):
            pre, curr = preOrderList[i - 1], preOrderList[i]
            pre.left = None
            pre.right = curr
