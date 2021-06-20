# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-19 15:39:23
# @Last Modified by:   polly
# @Last Modified time: 2021-06-19 16:34:56

# 回文数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (k := str(x)) == k[::-1]
