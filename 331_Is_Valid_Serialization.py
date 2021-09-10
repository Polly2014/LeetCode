# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-10 21:54:04
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-10 22:28:23

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for node in preorder.split(','):
            stack.append(node)
            while len(stack) > 2 and stack[-2] == '#' and stack[-1] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
            print(stack)
        if len(stack) == 1 and stack[0] == '#':
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
