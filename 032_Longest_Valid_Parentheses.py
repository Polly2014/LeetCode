# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-04 16:57:06
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-04 17:48:25
class Solution:
        # 动态规划
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)

    # 栈
    def longestValidParentheses(self, s: str) -> int:
        stack = [(-1, None)]
        length, max_length = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((i, s[i]))
            else:
                stack.pop()
                if stack == []:
                    stack.append((i, s[i]))
                else:
                    length = i - stack[-1][0]
                    max_length = max(max_length, length)
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses('())((())'))
