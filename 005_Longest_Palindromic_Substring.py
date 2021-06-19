# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-18 21:41:19
# @Last Modified by:   polly
# @Last Modified time: 2021-06-18 22:41:57

class Solution:
    # 暴力穷举
    # def longestPalindrome(self, s: str) -> str:
    #     ans = s[0]
    #     n = len(s)
    #     for i in range(n - 1):
    #         for j in range(i + 1, n + 1):
    #             if s[i:j] == s[j:i:-1] and j - i >= len(ans):
    #     return ans

    # 中心扩散
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_left, max_right = 0, 0
        for i in range(n):
            length_1 = self.expandAroundCenter(s, i, i)
            length_2 = self.expandAroundCenter(s, i, i + 1)
            max_length = max(length_1, length_2)
            if max_length > (max_right - max_left):
                max_left = i - (max_length - 1) // 2
                max_right = i + max_length // 2
        return s[max_left:max_right + 1]

    def expandAroundCenter(self, s, left, right):
        n = len(s)
        while(left >= 0 and right < n and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("cbbd"))
