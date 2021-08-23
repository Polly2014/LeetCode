# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-22 15:32:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-22 15:43:47
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        # print('Stack Status: {}'.format(stack))
        for x in s:
            if x == '(':
                stack.append(0)
                # print('\t 当前( 入栈')
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
            #     print('\t 当前) 出栈， 修改栈顶元素{}->{}'.format(v, stack[-1]))
            # print('Stack Status: {}'.format(stack))
            # print('-------------------------')
        return stack.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses('(()(()))'))
