# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-09 21:05:21
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-09 21:54:05
import re
from collections import deque
class Solution:

    # BFS
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            n = 1
            while n:
                s, n = re.subn(r'(.)\1{2,}', '', s)
            return s
        # 将手中的球排序
        hand = ''.join(sorted(hand))
        # 状态队列（桌面状态，手中状态，回合数）
        Q = deque([(board, hand, 0)])
        # 访问记录集
        visited = {(board, hand)}
        # BFS
        while Q:
            cur_board, cur_hand, step = Q.popleft()
            # 两重for循环的新写法
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # 第1个剪枝条件：手中当前球和上一个球颜色相同
                if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                    continue
                # 第2个剪枝条件：桌面上只在连续相同颜色球的开始位置插入新球
                if i > 0 and cur_board[i - 1] == cur_hand[j]:
                    continue
                # 第3个剪枝条件：只在以下两种情况下放置新球
                #  - 情况1: 当前球与后面球颜色相同
                #  - 情况2: 前后颜色相同，且与当前颜色不同时放置球
                choose = False
                if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                    choose = True
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    choose = True
                if choose:
                    new_board = clean(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    if not new_board:
                        return step + 1
                    if (new_board, new_hand) not in visited:
                        Q.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))
        return -1

    # DFS+记忆化

    def findMinStep(self, board: str, hand: str) -> int:
        ans = self.DFS(board, ''.join(sorted(hand)))
        return ans if ans <= 5 else -1

    @lru_cache(None)
    def DFS(self, cur_board, cur_hand):
        if not cur_board:
            return 0
        res = 6
        for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
            if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                continue
            if i > 0 and cur_board[i - 1] == cur_hand[j]:
                continue
            choose = False
            if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                choose = True
            if i < len(cur_board) and cur_board[i] == cur_board[j]:
                choose = True
            if choose:
                new_board = self.clean(cur_board[:i] + cur_hand[j] + cur_board[i:])
                new_hand = cur_hand[:j] + cur_hand[j + 1:]
                res = min(res, self.DFS(new_board, new_hand) + 1)
        return ans

    @staticmethod
    def clean(s):
        n = 1
        while n:
            s, n = re.subn(r'(.)\1{2,}', '', s)
        return s
