# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-27 22:27:32
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-27 23:31:39
class Solution:
    def numDecodings(self, s: str) -> int:
        def judge(ss):
            if len(ss) == 1:
                if ss == '*':
                    return 9
                elif ss == '0':
                    return 0
                else:
                    return 1
            elif len(ss) == 2:
                if ss == '**':
                    return 9 + 6
                elif ss[0] == '*':
                    return 2 if '1' <= ss[1] <= '6' else 2 if ss[1] == '0' else 1
                elif ss[1] == '*':
                    return 9 if ss[0] == '1' else 6 if ss[0] == '2' else 0
                elif ss[0] in '12':
                    return 1 if '09' < ss < '27' else 0
                else:
                    return 0
        n = len(s)
        MOD = 1e9 + 7
        dp = [0] * n
        dp[0] = 9 if s[0] == '*' else 0 if s[0] == '0' else 1
        for i in range(1, n):
            print('One str: {}'.format(dp[i - 1] * judge(s[i])))
            print('Two str: {}'.format(dp[max(i - 2, 0)] * judge(s[i - 1:i + 1])))
            dp[i] += int(dp[i - 1] * judge(s[i]) % MOD)
            dp[i] += int(dp[i - 2] * judge(s[i - 1:i + 1]) % MOD if i - 2 >= 0 else judge(s[i - 1:i + 1]) % MOD)
            dp[i] = int(dp[i] % MOD)
        print(dp)
        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    s.numDecodings('*10*1')
