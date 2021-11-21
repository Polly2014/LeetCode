# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-18 22:11:22
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-18 23:09:08
from pysnooper import snoop
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0

        def DFS(node):
            # 返回值（自身坡度，当前节点为根的坡度之和）
            if not node:
                return 0
            # 左子树之和
            sum_left = DFS(node.left)
            # 右子树之和
            sum_right = DFS(node.right)
            nonlocal ans
            # 总坡度存放在全局变量中
            ans += abs(sum_left - sum_right)
            # 返回当前根节点的子树之和
            return sum_left + sum_right + node.val
        DFS(root)
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, left=None, right=TreeNode(7)))
    print(s.findTilt(root))
