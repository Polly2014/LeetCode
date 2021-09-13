# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-13 22:04:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-13 22:15:29
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 判断根节点为空的情况
        if not p and not q:
            return True
        # 判断根节点有一个为空的情况
        if not p or not q:
            return False
        # 两根节点均不为空，判断根节点的值
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
