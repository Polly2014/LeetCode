# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 10:44:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-20 14:48:51
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def DFS(curr, count):
                # 终止条件
            if not curr.left and not curr.right:
                return True if count == 0 else False
            # 单层递归逻辑(左)
            if curr.left:
                count -= curr.left.val
                if DFS(curr.left, count):
                    return True
                count += curr.left.val
            # 单层递归逻辑(右)
            if curr.right:
                count -= curr.right.val
                if DFS(curr.right, count):
                    return True
                count += curr.right.val
            return False
