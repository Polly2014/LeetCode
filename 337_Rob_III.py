# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-27 23:10:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-28 21:37:55

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def robTree(node):
            if not node:
                return [0, 0]
            leaf_l = robTree(node.left)
            leaf_r = robTree(node.right)
            return [max(leaf_l) + max(leaf_r), node.val + leaf_l[0] + leaf_r[0]]

        return max(robTree(root))
