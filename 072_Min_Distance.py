# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-23 22:29:49
# @Last Modified by:   polly
# @Last Modified time: 2021-06-23 23:04:09

# 编辑距离

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp_distance = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp_distance[i][0] = i
        for j in range(n + 1):
            dp_distance[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp_distance[i][j] = dp_distance[i - 1][j - 1]
                else:
                    dp_distance[i][j] = min(dp_distance[i - 1][j], dp_distance[i][j - 1], dp_distance[i - 1][j - 1]) + 1
        return dp_distance[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('horse', 'ros'))
