# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-10 23:31:41
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-11 11:41:32

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = -float('inf')

    def maxPathSum(self, root: TreeNode) -> int:

        def DFS(node):
            if not node:
                return 0
            left = max(DFS(node.left), 0)
            right = max(DFS(node.right), 0)
            self.ans = max(self.ans, left + node.val + right)
            return node.val + max(left, right)
        DFS(root)
        return self.ans
