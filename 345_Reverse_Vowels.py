# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-19 23:22:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-19 23:31:16
class Solution:
    def reverseVowels(self, s: str) -> str:
        WORDS = 'aeiouAEIOU'
        s = list(s)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] in WORDS and s[r] in WORDS:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                continue
            if s[l] not in WORDS:
                l += 1
            if s[r] not in WORDS:
                r -= 1
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels('hello'))
