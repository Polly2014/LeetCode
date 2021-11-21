# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-21 14:13:08
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-21 14:15:49

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return max([self.maxDepth(c) for c in root.children] + [0]) + 1
