# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 00:39:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 15:47:58

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     nodes = []

    #     def DFS(node):
    #         if not node:
    #             return
    #         DFS(node.left)
    #         nodes.append(node)
    #         DFS(node.right)
    #     DFS(root)
    #     x, y = None, None
    #     pre = nodes[0]
    #     for i in range(1, len(nodes)):
    #         if pre.val > nodes[i].val:
    #             y = nodes[i]
    #             if not x:
    #                 x = pre
    #         pre = nodes[i]

    #     if x and y:
    #         x.val, y.val = y.val, x.val

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def DFS(node):
            if not node:
                return
            DFS(node.left)
            nodes.append(node)
            DFS(node.right)
        DFS(root)
        x, y = None, None
        for i in range(1, len(nodes)):
            if nodes[i - 1].val > nodes[i].val:
                if not x:
                    x = nodes[i - 1]
                y = nodes[i]

        if x and y:
            x.val, y.val = y.val, x.val
