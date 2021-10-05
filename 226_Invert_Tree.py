# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-05 19:17:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-05 19:26:46
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

    # BFS

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        Q = [root]
        while Q:
            node = Q.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        return root

    # DFS

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
