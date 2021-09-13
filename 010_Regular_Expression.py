# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-20 22:55:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-14 00:16:40

# 动态规划、记忆递归、重叠子问题
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # s为字符串，不含特殊字符，因此空无法变成s任意非空子串，保持False，无需操作
        # 空字符串，只能和*匹配串
        for i in range(m + 1):
            for j in range(1, n + 1):
                # p当前字符为'*'
                if p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                # p当前字符为'.'或普通字符
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    s.isMatch('aa', 'a*')
