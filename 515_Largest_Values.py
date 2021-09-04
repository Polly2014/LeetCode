# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 16:57:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 16:57:13
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
