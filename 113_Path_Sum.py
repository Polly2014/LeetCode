# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 10:44:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-26 11:35:45
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
        if not root:
            return []
        ans = []
        path = [root.val]

        def BackTracking(curr, count):
            # 终止条件 (到达叶子节点，即左右子树均为空)
            if not curr.left and not curr.right:
                if count == 0:
                    ans.append(path[:])
                return
            # 单层递归逻辑(左)
            if curr.left:
                path.append(curr.left.val)
                count -= curr.left.val
                BackTracking(curr.left, count)
                count += curr.left.val
                path.pop()
            # 单层递归逻辑(右)
            if curr.right:
                path.append(curr.right.val)
                count -= curr.right.val
                BackTracking(curr.right, count)
                count += curr.right.val
                path.pop()
            # return
        BackTracking(root, targetSum - root.val)
        return ans

        # 方法二：DFS
        # def DFS(node, count):
        #     if not root:
        #         return
        #     if not root.left and not root.right and count == root.val:
        #         return True
        #     return DFS(root.left, count - root.val) or DFS(root.right, count - root.val)
