# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-18 13:34:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-18 22:56:16
class Solution:
    # def checkRecord(self, n: int) -> int:
    #     MOD = 1e9 + 7
    #     memory = [[[0] * 2 for _ in range(3)] for _ in range(n)]

    #     def DFS(idx, num_late, num_absent):
    #         if idx >= n:
    #             return 1
    #         if memory[idx][num_late][num_absent] != 0:
    #             return memory[idx][num_late][num_absent]
    #         ans = 0
    #         ans += DFS(idx + 1, num_late, num_absent) % MOD
    #         if num_absent < 1:
    #             ans += DFS(idx + 1, num_late, num_absent + 1) % MOD
    #         if num_late < 2:
    #             ans += DFS(idx + 1, num_late + 1, num_absent) % MOD
    #         memory[idx][num_late][num_absent] = int(ans % MOD)
    #         return int(ans % MOD)
    #     ans = DFS(0, 0, 0)
    #     return ans

    # def checkRecord(self, n: int) -> int:
    #     MOD = 1e9 + 7

    #     def DFS(idx, num_late, num_absent):
    #         if idx >= n:
    #             return 1
    #         ans = 0
    #         ans += DFS(idx + 1, num_late, num_absent) % MOD
    #         if num_absent > 0:
    #             ans += DFS(idx + 1, num_late, num_absent - 1) % MOD
    #         if num_late > 0:
    #             ans += DFS(idx + 1, num_late - 1, num_absent) % MOD
    #         return int(ans % MOD)
    #     ans = DFS(0, 2, 1)
    #     return ans

    # def checkRecord(self, n: int) -> int:
    #     MOD = 1e9 + 7
    #     memory = [[[0] * 2 for _ in range(3)] for _ in range(n)]

    #     def DFS(idx, num_late, num_absent):
    #         if idx >= n:
    #             return 1
    #         if memory[idx][num_late][num_absent] != 0:
    #             return memory[idx][num_late][num_absent]
    #         ans = 0
    #         ans += DFS(idx + 1, num_late, num_absent) % MOD
    #         if num_absent > 0:
    #             ans += DFS(idx + 1, num_late, num_absent - 1) % MOD
    #         if num_late > 0:
    #             ans += DFS(idx + 1, num_late - 1, num_absent) % MOD
    #         memory[idx][num_late][num_absent] = ans
    #         return int(ans % MOD)
    #     ans = DFS(0, 2, 1)
    #     return ans

    def checkRecord(self, n: int) -> int:
        MOD = 1e9 + 7
        # dp[i][absent][late]
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        dp[0][1][0] = 1
        for i in range(1, n):
            # 0-absent , 0-late
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD
            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][0] = (dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2] +
                           dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD
            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][2] = dp[i - 1][1][1]
        return int(sum([sum(d) % MOD for d in dp[n - 1]]) % MOD)


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord(2))
