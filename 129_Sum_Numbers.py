# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-07 00:07:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-07 00:21:54
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归｜DFS
    def sumNumbers(self, root: TreeNode) -> int:
        def DFS(node, sumTotal):
            if not node:
                return 0
            sumTotal = sumTotal * 10 + node.val
            if not node.left and not node.right:
                return sumTotal
            return DFS(node.left, sumTotal) + DFS(node.right, sumTotal)
        return DFS(root, 0)
