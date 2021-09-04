# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 16:51:00
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 16:52:54

from typing import List
# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if node.children:
                    q.extend(node.children)
            ans.append(ans_level)
        return ans
