# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-24 13:14:16
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-05 12:58:26
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 迭代法
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = root.left if p.val < root.val else root.right
        return root

    # 递归
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return root if (root.val - p.val) * (root.val - q.val) > 0 else lowestCommonAncestor(root.left if p.val < root.val else root.right, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val - p.val) * (root.val - q.val) > 0:
            return root
        return lowestCommonAncestor(root.left if p.val < root.val else root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root # 中止处理
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q) # 左
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q) # 右
        else:
            return root # 中
