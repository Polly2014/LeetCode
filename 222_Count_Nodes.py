# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-12 11:57:25
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-12 11:59:10

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def count_nodes(node):
            if not node:
                return 0
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            return left + right + 1
        return count_nodes(root)
