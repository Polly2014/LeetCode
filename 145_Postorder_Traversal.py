# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 00:51:28
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-20 00:56:57
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def DFS(node):
            if not node:
                return
            DFS(node.left)
            DFS(node.right)
            ans.append(node.val)
        DFS(root)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.postorderTraversal([1, null, 2, 3])
