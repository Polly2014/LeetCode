# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-13 22:44:36
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-13 23:14:07
from typing import List
from collections import defaultdict
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = defaultdict(int)

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def findTreeSum(root):
            if not root:
                return 0
            cur_sum = root.val + findTreeSum(root.left) + findTreeSum(root.right)
            self.ans[cur_sum] += 1
            return cur_sum
        findTreeSum(root)
        max_cnt = max(self.ans.values())
        return [k for k, v in self.ans.items() if v == max_cnt]
