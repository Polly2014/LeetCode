# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 18:48:03
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-20 23:03:15
from typing import List
from collections import deque
from pprint import pprint
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1)
        pNode.right = creatBTree(data, 2 * index + 2)
    return pNode


class Solution:
    # BFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            node = q[-1]
            ans.append(node.val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
    # DFS
    def rightSideView(self, root: TreeNode) -> List[int]:


if __name__ == '__main__':
    s = Solution()
    data = [1, 2, 3, None, 5, None, 4]
    root = creatBTree(data, 0)
    print(s.rightSideView(root))
