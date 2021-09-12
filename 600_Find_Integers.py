# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-11 21:59:31
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-11 22:31:29

class Solution:
    def findIntegers(self, n: int) -> int:
        n_bin = bin(n)[2:]
        N = len(n_bin)
        dp = [0 for _ in range(N + 1)]
        dp[0], dp[1] = 1, 2
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        ans = 0
        for i, num in enumerate(n_bin):
            if num == '1':
                ans += dp[N - i - 1]
                if i > 0 and n_bin[i - 1] == '1':
                    return ans
        return ans + 1

    @lru_cache(None)
    def findIntegers(self, n: int) -> int:
        if n <= 3:
            return n + 1 if n < 3 else n
        bits = len(bin(n)) - 2
        return self.findIntegers((1 << (bits - 1)) - 1) + (self.findIntegers((1 << (bits - 2)) - 1) if (n >> (bits - 2)) & 1 else self.findIntegers(n - (1 << (bits - 1))))


if __name__ == '__main__':
    s = Solution()
    print(s.findIntegers(5))
