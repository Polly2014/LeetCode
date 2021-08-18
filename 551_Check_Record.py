# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-17 22:43:00
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-17 22:44:53
class Solution:
    def checkRecord(self, s: str) -> bool:
        return 'LLL' not in s and s.count('A') < 3
if __name__=='__main__':
	s = Solution()
	print(s.checkRecord('AA'))