# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-10 16:50:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-10 17:02:09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False if subRoot else True
        if root.val == subRoot.val:
            return self.isSametree(root, subRoot)
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)

    def isSametree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.isSametree(root1.left, root2.left) and self.isSametree(root1.right, root2.right)
        return False
