# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 18:38:55
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 19:55:01
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])

        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx + 1:-1])

        return root
