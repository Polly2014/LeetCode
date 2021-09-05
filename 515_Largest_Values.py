# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 16:57:01
# @Last Modified by:   polly
# @Last Modified time: 2021-09-05 15:34:11
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            n = len(q)
            ans_level = []

            for _ in range(n):
                node = q.pop(0)
                ans_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max(ans_level))
        return ans
