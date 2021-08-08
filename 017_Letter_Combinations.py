# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-08 10:43:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-08 11:04:45
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans, path = [], []
        if not digits:
            return []

        def BackTracking(path, idx):
            if idx == len(digits):
                ans.append(''.join(path))
            else:
                for d in digit_map[digits[idx]]:
                    BackTracking(path + [d], idx + 1)
        BackTracking(path, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('2234'))
