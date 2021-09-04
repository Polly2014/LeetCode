# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 15:57:41
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 16:21:55
from typing import List
# Definition for a binary tree node.
from queue import deque
# DFS 相较于 BFS要简洁很多，因为递归的方式隐含的使用了系统的栈，我们不需要自己维护一个数据结构


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        ans_level = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ans_level.append(node.val)
            ans.append(ans_level)
            ans_level = []

        return ans
