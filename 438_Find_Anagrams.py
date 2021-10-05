# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-06 00:36:59
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-06 00:41:31
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        cnt_p = Counter(p)
        ans = []
        for i in range(m - n + 1):
            if Counter(s[i:i + n]) == cnt_p:
                ans.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams('abab', 'ab'))


# if __name__ == '__main__':
#     print(set([1, 2]) == set([2, 1]))
