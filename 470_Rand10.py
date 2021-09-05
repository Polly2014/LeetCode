# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-05 21:45:02
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-05 21:51:00
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1
            else:
                continue
