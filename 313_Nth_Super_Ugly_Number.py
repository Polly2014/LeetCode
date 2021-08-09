# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-09 14:18:15
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-09 18:48:11
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 存放丑数结果的数组
        dp = [1] * n
        # 记录因子，及与丑数数组相乘的下标
        prime_with_idx = [[prime, 0] for prime in primes]
        # 开始遍历更新DP数组
        for i in range(1, n):
            prime, offset = min(prime_with_idx, key=lambda x: x[0] * dp[x[1]])
            dp[i] = prime * dp[offset]
            for p in prime_with_idx:
                if p[0] * dp[p[1]] == dp[i]:
                    p[1] += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
