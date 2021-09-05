# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-05 22:11:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-05 22:45:21
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS深度优先
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        return max(leftHeight, rightHeight) + 1

    # BFS广度优先
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        Q = [root]
        while Q:
            print('ans: {}, Q: {}'.format(ans, [q.val for q in Q]))
            n = len(Q)
            ans += 1
            for _ in range(n):
                node = Q.pop(0)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return ans

    def build_tree_from_list(self, value_list):
        n = len(value_list)

        def make_tree(node, i):
            if i < n:
                if value_list[i] in ['#', None]:
                    return None
                else:
                    node = TreeNode(value_list[i])
                    node.left = make_tree(node.left, 2 * i + 1)
                    node.right = make_tree(node.right, 2 * i + 2)
                    return node
            return node
        root = TreeNode(0)
        root = make_tree(root, 0)
        return root


if __name__ == '__main__':
    s = Solution()
    root = s.build_tree_from_list([1, 2, 3, 4, None, None, 5])
    print(s.maxDepth(root))
