# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-14 22:39:25
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-14 23:15:50
from typing import List


class Solution:
    # 经典DP
    # def generateParenthesis(self, n: int) -> List[str]:
    #     dp = [[] for _ in range(n + 1)]
    #     dp[0].append('')
    #     dp[1].append('()')
    #     for i in range(2, n + 1):
    #         for left in range(i):
    #             right = i - left - 1
    #             for l in dp[left]:
    #                 for r in dp[right]:
    #                     dp[i].append('(' + l + ')' + r)
    #     return dp[-1]

    # DFS
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def DFS(path, num_left, num_right):
            if num_left == num_right == 0:
                ans.append(path)
                return
            if num_left > num_right:
                return
            if num_left > 0:
                DFS(path + '(', num_left - 1, num_right)
            if num_right > 0:
                DFS(path + ')', num_left, num_right - 1)
        DFS('', 5, 5)
        return(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(5))
