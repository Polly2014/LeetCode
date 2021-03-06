# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-03 23:37:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 00:26:36
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []

        def DFS(node):
            if not node:
                return
            DFS(node.left)
            ans.append(node.val)
            DFS(node.right)
        DFS(root)

        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        def BFS(root, left, right):
            if root is None:
                return True

            if left < root.val < right:
                return BFS(root.left, left, root.val) and BFS(root.right, root.val, right)
            else:
                return False

        return BFS(root, -float('inf'), float('inf'))
