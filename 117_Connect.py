# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-04 17:06:15
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-04 17:15:21
from typing import List
# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # 本句很妙
                if i == n - 1:
                    break
                node.next = q[0]
        return root
