# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-18 21:41:19
# @Last Modified by:   polly
# @Last Modified time: 2021-06-18 21:45:47

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [[0] * n for i in range(n)]

        for i in range(n):
            ans[i][i] = 1
        for i in range(n - 1):
            if ans[i] == ans[i + 1]:
                ans[i][i + 1] = 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    s = 'aba'
    print(solution.longestPalindrome(s))
