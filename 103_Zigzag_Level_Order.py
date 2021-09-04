# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 21:05:55
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 21:11:41
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        Q = [root]
        while Q:
            n = len(Q)
            ans_level = []
            for _ in range(n):
                node = Q.pop(0)
                ans_level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            ans.append(ans_level)
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
        return ans
