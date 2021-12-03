# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-26 21:18:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-26 21:20:17
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val==val:
            return root
        elif root.val<val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)