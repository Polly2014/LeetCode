# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-20 19:12:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-20 21:07:09
from pysnooper import snoop


class Solution:
    def __init__(self):
        self.ans = 0
        self.record = {}

    # 回溯
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @snoop()
        def BackTracking(startIndex):
            if startIndex == n:
                return 1
            if s[startIndex] == '0':
                return 0
            if startIndex in self.record:
                return self.record[startIndex]
            res = 0
            for i in range(1, 3):
                if startIndex + i > n:
                    break
                ss = s[startIndex:startIndex + i]
                if not 1 <= int(ss) <= 26:
                    break
                res += BackTracking(startIndex + i)
                self.record[startIndex + i] = res
            return res
        self.ans = BackTracking(0)
        return self.ans

    # 再来一般DP
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 0 if s[0] == '0' else 1

        for i in range(1, n):
            # 一位
            if s[i] != '0':
                dp[i] = dp[i - 1]
            # 两位
            if s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[max(i - 2, 0)]
        print(s)
        print(dp)
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("226"))
