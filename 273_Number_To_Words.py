# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-11 21:48:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-11 22:23:43
singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
        # 递归
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        def recursion(num):
            s = ''
            if num == 0:
                return s
            elif num < 10:
                s += singles[num] + ' '
            elif num < 20:
                s += teens[num - 10] + ' '
            elif num < 100:
                s += tens[num // 10] + ' ' + recursion(num % 10)
            else:
                s += singles[num // 100] + ' Hundred ' + recursion(num % 100)
            return s

        s = ''
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num -= curNum * unit
                s += recursion(curNum) + thousands[i] + ' '
            unit //= 1000
        return s.strip()

    # 单词拼写
    def numberToWords(self, num: int) -> str:
        billion = int(1e9)
        million = int(1e6)
        thousand = int(1e3)
        hundred = int(100)
        map_digit = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                     15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        if num == 0:
            return 'Zero'
        s = ''
        if num >= billion:
            s += self.numberToWords(num // billion)
            s += ' Billion'
            num %= billion
        if num >= million:
            if len(s):
                s += ' '
            s += self.numberToWords(num // million)
            s += ' Million'
            num %= million
        if num >= thousand:
            if len(s):
                s += ''
            s += self.numberToWords(num // thousand)
            s += ' Thousand'
            num %= thousand
        if num >= hundred:
            if len(s):
                s += ' '
            s += self.numberToWords(num // hundred)
            s += ' Hundred'
            num %= hundred
        for k, v in reversed(map_digit.items()):
            if num >= k:
                num -= k
                if len(s):
                    s += ' '
                s += v
        return s
