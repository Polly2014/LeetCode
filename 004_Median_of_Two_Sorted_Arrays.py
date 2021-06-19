# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-17 22:39:14
# @Last Modified by:   polly
# @Last Modified time: 2021-06-18 00:11:04

# 两个有序数组，求整体中位数（核心：第k小数字）
#  - 如果对时间复杂度的要求有 log，通常都需要用到二分查找
#  - 因此，这道题可以转化成寻找两个有序数组中的第k小的数，其中k为(m+n)/2或(m+n)/2+1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 将较短的数组放前面
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 统计两个数组长度，且维持（m<=n）
        m, n = len(nums1), len(nums2)

        # 分割线左边的数字总个数
        total_left = (m + n + 1) // 2

        # 定义分割线(交叉小于)
        # 再nums1的区间[0, m]中寻找分割线，使得 nums1[i-1]<=nums2[j] && nums2[j-1]>=nums1[i]
        left, right = 0, m

        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                # 下一轮搜索区间[left, i-1]
                right = i - 1
            else:
                # 下一轮搜索区间[i, right]
                left = i

        i, j = left, total_left - left
        nums1_left_max = MAX if i == 0 else nums1[i - 1]
        nums1_right_min = MIN if i == m else nums1[i]
        nums2_left_max = MAX if j == 0 else nums2[j - 1]
        nums2_right_min = MIN if j == n else nums2[j]

        return max(nums1_left_max, nums2_right_min) if (m + n + 1) % 2 == 0 else (max(nums1_left_max, nums2_right_min) + max(nums1_right_min, nums2_left_max)) / 2.
