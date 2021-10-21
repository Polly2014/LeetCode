# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-21 20:12:11
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-21 20:23:43
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从后往前，找到第一个不为9的数
        for i in range(n:=len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                for j in range(i+1,n+1):
                    digits[j]=0
                return digits
        return [1]+[0]*len(digits)