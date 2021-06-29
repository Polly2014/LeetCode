# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-28 23:35:23
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-28 23:50:37
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j] == True:
                    dp[i] = True
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
