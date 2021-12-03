# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-25 23:06:41
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-03 22:31:22
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    	# 在 buckets 桶液体中恰好有一桶有毒，至少需要多少只小猪才能在 iterations 轮测试中确定有毒的是哪一桶
    	if buckets == 1:
            return 0
        combinations = [[0] * (buckets + 1) for _ in range(buckets + 1)]
        combinations[0][0] = 1
        iterations = minutesToTest // minutesToDie
        # f(i,j): i只小猪测试j轮，最多可以再多少桶液体中确定有毒的是哪一桶
        # 当j固定时，我们需要计算获得f(i,j)>=buckets成立的最小的i
        f = [[1] * (iterations + 1)] + [[1] + [0] * iterations for _ in range(buckets - 1)]
        for i in range(1, buckets):
            combinations[i][0] = 1
            for j in range(1, i):
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j]
            combinations[i][i] = 1
            for j in range(1, iterations + 1):
                for k in range(i + 1):
                    f[i][j] += f[k][j - 1] * combinations[i][i - k]
            if f[i][iterations] >= buckets:
                return i
        return 0