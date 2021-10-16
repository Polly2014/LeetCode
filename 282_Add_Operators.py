# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-16 19:19:12
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-16 22:59:33
from typing import List
from pysnooper import snoop
import re


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        # @snoop()
        def BackTracking(expr, startIndex, res, mul):
            # @expr: 表达式字符串
            # @startIndex: 遍历到第几个数字
            # @res: 当前结果
            # @mul: 最后连乘结果
            if startIndex == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            # 当前表达式长度
            signIndex = len(expr)
            # 如果不是第一个，那就先加入一个占位操作符
            if startIndex > 0:
                expr.append('')
            val = 0
            for i in range(startIndex, n):
                if i > startIndex and num[startIndex] == '0':
                    break
                val = val * 10 + int(num[i])
                expr.append(num[i])
                # 表达式开头不能添加符号
                if startIndex == 0:
                    BackTracking(expr, i + 1, val, val)
                else:  # 枚举符号
                    expr[signIndex] = '+'
                    BackTracking(expr, i + 1, res + val, val)
                    expr[signIndex] = '-'
                    BackTracking(expr, i + 1, res - val, -val)
                    expr[signIndex] = '*'
                    BackTracking(expr, i + 1, res - mul + mul * val, mul * val)
            print(expr)
            del expr[signIndex:]
            print(expr)
            print('-' * 30)
        BackTracking([], 0, 0, 0)
        return ans

    o, ptn = ['', '+', '-', '*'], re.compile(r'[\D]0\d')

    def addOperators(self, num: str, target: int) -> List[str]:
        def check(expr): return not ptn.search('+' + expr) and eval(expr) == target
        return [expr for expr in [''.join(chain(*zip_longest(num, ops, fillvalue=''))) for ops in product(o, repeat=len(num) - 1)] if check(expr)]

    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []
        path = []

        @snoop()
        def BackTracking(startIndex, cur_sum, pre_add):
            nonlocal ans, path
            if startIndex == n:
                if cur_sum == target:
                    ans.append(''.join(path[:]))
                return
            # 当前表达式长度
            pn = len(path)
            for i in range(startIndex, n):
                x_str = num[startIndex:i + 1]
                x = int(x_str)

                if startIndex == 0:
                    path += x_str
                    BackTracking(i + 1, cur_sum + x, x)
                    path = path[:pn]
                else:
                    path += '+' + x_str
                    BackTracking(i + 1, cur_sum + x, x)
                    path = path[:pn]

                    path += '-' + x_str
                    BackTracking(i + 1, cur_sum - x, -x)
                    path = path[:pn]

                    path += '*' + x_str
                    BackTracking(i + 1, cur_sum - pre_add + pre_add * x, pre_add * x)
                    path = path[:pn]
                if x == 0:
                    return
        BackTracking(0, 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.addOperators('1234', 5))
