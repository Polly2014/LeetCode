# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-21 14:13:08
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-21 22:10:11

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


if __name__ == '__main__':
    print('KS: {:.2f}'.format(50 / 14.))
    print('ST: {:.2f}+{:.2f}+{:.2f}'.format(65 / 15., 10 / 12, 20 / 4 / 12))
    print('MS: {:.2f}+{:.2f}+{:.2f}+{:.2f}'.format(42 / 12., 44.75 / 4 / 12, 3.836 / 12, 1.23 / 12))
    print('HW: {:.2f}'.format(4.3))
