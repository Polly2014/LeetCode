# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-10 22:43:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-10 23:03:40
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        path = []

        def DFS(node):
            # 中止条件判断
            if not node:
                return

            # 单层循环处理逻辑
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append(path[:])
                return

            if node.left:
                DFS(node.left)
                path.pop()
            if node.right:
                DFS(node.right)
                path.pop()
        DFS(root)
        ans = ['->'.join(path) for path in ans]
        return ans
