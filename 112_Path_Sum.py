# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 10:44:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-26 11:08:08
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # 方法一：回溯（即有撤回）
        # def BackTracking(curr, count):
        #     # 终止条件
        #     if not curr.left and not curr.right:
        #         return True if count == 0 else False
        #     # 单层递归逻辑(左)
        #     if curr.left:
        #         count -= curr.left.val
        #         if BackTracking(curr.left, count):
        #             return True
        #         count += curr.left.val
        #     # 单层递归逻辑(右)
        #     if curr.right:
        #         count -= curr.right.val
        #         if BackTracking(curr.right, count):
        #             return True
        #         count += curr.right.val
        #     return False
        # return BackTracking(root, targetSum)

        # 方法二：DFS
        def DFS(node, count):
            if not root:
                return
            if not root.left and not root.right and count == root.val:
                return True
            return DFS(root.left, count - root.val) or DFS(root.right, count - root.val)
