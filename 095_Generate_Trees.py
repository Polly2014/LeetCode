# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-01 20:47:08
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-01 22:51:25
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTree(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTree = generateTree(start, i - 1)
                rightTree = generateTree(i + 1, end)

                for l in leftTree:
                    for r in rightTree:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        return generateTree(1, n) if n else []

    def generateTrees(self, n: int) -> List[TreeNode]:
        def makeTree(start, end):
            ans = []
            for i in range(start, end):
                leftTrees, rightTrees = [None], [None]
                if i > start:
                    leftTrees = makeTree(start, i)
                if i < end - 1:
                    rightTrees = makeTree(i + 1, end)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        node = TreeNode(i, leftTree, rightTree)
                        ans.append(node)
            return ans

        return makeTree(1, n + 1)
