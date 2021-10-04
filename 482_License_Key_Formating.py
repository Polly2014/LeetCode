# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-04 16:37:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-04 16:45:48
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()[::-1]
        ans = [s[i:i + k] for i in range(0, len(s), k)]
        return '-'.join(ans)[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting('5F3Z-2e-9-w', 4))
