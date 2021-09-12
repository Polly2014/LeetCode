# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-12 11:28:35
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-12 11:48:45
class Solution:
    def checkValidString(self, s: str) -> bool:
        # 解法一：贪心法
        # n = len(s)
        # left, right = 0, 0
        # for i in range(n):
        #     left += (-1) if s[i] == ')' else 1
        #     right += (-1) if s[n - i - 1] == '(' else 1
        #     if left < 0 or right < 0:
        #         return False
        # return True

        # 解法二：双栈法
        stack_left, stack_star = [], []
        for i, ss in enumerate(s):
            if ss == '(':
                stack_left.append(i)
            elif ss == '*':
                stack_star.append(i)
            else:
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        while stack_left:
            if not stack_star:
                return False
            elif stack_left[-1] > stack_star[-1]:
                return False
            else:
                stack_left.pop()
                stack_star.pop()
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
