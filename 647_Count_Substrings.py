# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 23:56:21
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-01 00:16:44
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # DP数组含义dp[i][j]，s[i:j+1]的回文子串
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        ans += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        ans += 1
        print(dp)
        print(ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.countSubstrings('abc')
