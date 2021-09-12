# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-12 13:55:32
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-12 14:00:12
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        return self.calcPathSum(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def calcPathSum(self, node, targetSum):
        if not node:
            return 0
        targetSum -= node.val
        if targetSum == 0:
            return 1 + self.calcPathSum(node.left, targetSum) + self.calcPathSum(node.right, targetSum)
        else:
            return self.calcPathSum(node.left, targetSum) + self.calcPathSum(node.right, targetSum)
