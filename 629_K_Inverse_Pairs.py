# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-11 21:47:28
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-11 22:56:53
class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        # 答案取模，大概率是动态规划解法
        MOD = 10**9 + 7

        dp = [1] + [0] * k
        for i in range(2, n + 1):
            next_dp = [1] + [0] * k
            for j in range(1, k + 1):
                next_dp[j] = (next_dp[j - 1] + dp[j] - (dp[j - i] if j >= i else 0)) % MOD
            dp = next_dp
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.kInversePairs(5, 3))
