# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 16:36:55
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 16:39:20
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return []
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
            ans.append(ans_level)
        return ans[::-1]
