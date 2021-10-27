# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-27 20:43:06
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-27 23:25:36
from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    # 回溯
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        # 统计需要删除的左右括号个数
        rm_left, rm_right = 0, 0
        for ss in s:
            if ss == '(':
                rm_left += 1
            elif ss == ')':
                if rm_left == 0:
                    rm_right += 1
                else:
                    rm_left -= 1

        # 验证字符串的括号是否合法
        def isValid(s):
            cnt = 0
            for ss in s:
                if ss == '(':
                    cnt += 1
                elif ss == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        # 回溯，尝试删除
        @lru_cache(None)
        def BackTracking(s, startIndex, rm_left, rm_right):
            if rm_left == 0 and rm_right == 0:
                if isValid(s):
                    ans.append(s)
                return

            for i in range(startIndex, len(s)):
                # 剪枝
                if i > startIndex and s[i] == s[i - 1]:
                    continue
                # 剪枝
                if rm_left + rm_right > len(s) - i:
                    break
                # 尝试删掉一个左括号
                if rm_left > 0 and s[i] == '(':
                    BackTracking(s[:i] + s[i + 1:], i, rm_left - 1, rm_right)
                if rm_right > 0 and s[i] == ')':
                    BackTracking(s[:i] + s[i + 1:], i, rm_left, rm_right - 1)
        BackTracking(s, 0, rm_left, rm_right)
        return ans

    # BFS

    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for ss in s:
                if s == '(':
                    cnt += 1
                elif s == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = set(s)
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            # level = {s[:i]+s[i+1:] for s in level for i in range(len(s)) if s[i] in '()'}
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses('(r(()()('))
