# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-18 13:34:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-18 14:01:46
class Solution:
    # def checkRecord(self, n: int) -> int:
    #     MOD = 1e9 + 7

    #     def DFS(idx, num_late, num_absent):
    #         if idx > n:
    #             return 1
    #         ans = 0
    #         ans += DFS(idx + 1, num_late, num_absent) % MOD
    #         if num_absent < 1:
    #             ans += DFS(idx + 1, num_late, num_absent + 1) % MOD
    #         if num_late < 2:
    #             ans += DFS(idx + 1, num_late + 1, num_absent) % MOD
    #         return int(ans % MOD)
    #     ans = DFS(1, 0, 0)
    #     return ans

    def checkRecord(self, n: int) -> int:
        MOD = 1e9 + 7

        def DFS(idx, num_late, num_absent):
            if idx >= n:
                return 1
            ans = 0
            ans += DFS(idx + 1, num_late, num_absent) % MOD
            if num_absent > 0:
                ans += DFS(idx + 1, num_late, num_absent - 1) % MOD
            if num_late > 0:
                ans += DFS(idx + 1, num_late - 1, num_absent) % MOD
            return int(ans % MOD)
        ans = DFS(0, 2, 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord(3))
