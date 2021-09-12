# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-12 19:19:29
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-12 19:35:27
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # 根节点为空，直接返回空
        if not root:
            return
        # 目标节点大于当前节点值，应去右子树中删除
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # 目标节点小于当前节点值，应去左子树中删除
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # 目标节点等于当前节点值，需删除当前节点
        else:
            # 当前节点左子树为空，直接返回右节点
            if not root.left:
                return root.right
            # 当前节点右子树为空，直接返回左节点
            if not root.right:
                return root.left
            # 左、右子树均不为空，则将左子树挂在右子树的最左节点上，返回右子树
            temp = root.right
            while temp.left:
                temp = temp.left
            temp.left = root.left
            root = root.right
        return root
