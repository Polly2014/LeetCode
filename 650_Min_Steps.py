# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-19 12:30:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-19 12:45:44
from pysnooper import snoop


class Solution:
    @snoop()
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, int(i**(1 / 2)) + 1):
                print('i={},j={}'.format(i, j))
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    dp[i] = min(dp[i], dp[i // j] + j)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.minSteps(3))
