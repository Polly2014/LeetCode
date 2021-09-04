# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 20:54:23
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 20:59:59
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []

        def DFS(node):
            if not node:
                return
            DFS(node.left)
            ans.append(node.val)
            DFS(node.right)
        DFS(root)
        return ans[k - 1]

    # 递归
    def kthSmallest(self, root, k):
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]
