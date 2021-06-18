# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-18 23:01:18
# @Last Modified by:   polly
# @Last Modified time: 2021-06-18 23:24:30

# 数字反转

class Solution:
    # 我太垃圾了，妈的
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        x_str = str(x)
        if x_str[0] == '-':
            ans = int(x_str[0] + x_str[:0:-1])
        else:
            ans = int(x_str[::-1])
        return ans if -2**31 <= ans and ans <= 2**31 - 1 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-9))
