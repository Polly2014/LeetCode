# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-21 16:27:35
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-21 22:15:27

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    self.ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def DFS(node):
            if not node:
                return 0
            L = DFS(node.left)
            R = DFS(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1
        DFS(root)
        return self.ans - 1
