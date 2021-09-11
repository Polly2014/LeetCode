# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 10:44:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-11 22:01:22
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
            # 空节点判断
            if not root:
                return
            # 叶子节点判断
            if not root.left and not root.right and count == root.val:
                return True
            # 问题规模可缩小，DFS表示当前传入节点为根节点，到其叶子节点是否存在路径和为传入的长度值（返回True|False）
            return DFS(root.left, count - root.val) or DFS(root.right, count - root.val)
