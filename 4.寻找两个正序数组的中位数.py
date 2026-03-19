#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
# #二分法1

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         def getKthElement(k):
#             """
#             - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
#             - 这里的 "/" 表示整除
#             - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
#             - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
#             - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
#             - 这样 pivot 本身最大也只能是第 k-1 小的元素
#             - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
#             - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
#             - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
#             """
            
#             index1, index2 = 0, 0
#             while True:
#                 # 特殊情况
#                 if index1 == m:
#                     return nums2[index2 + k - 1]
#                 if index2 == n:
#                     return nums1[index1 + k - 1]
#                 if k == 1:
#                     return min(nums1[index1], nums2[index2])

#                 # 正常情况
#                 newIndex1 = min(index1 + k // 2 - 1, m - 1)
#                 newIndex2 = min(index2 + k // 2 - 1, n - 1)
#                 pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
#                 if pivot1 <= pivot2:
#                     k -= newIndex1 - index1 + 1
#                     index1 = newIndex1 + 1
#                 else:
#                     k -= newIndex2 - index2 + 1
#                     index2 = newIndex2 + 1
        
#         m, n = len(nums1), len(nums2)
#         totalLength = m + n
#         if totalLength % 2 == 1:
#             return getKthElement((totalLength + 1) // 2)
#         else:
#             return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



# #二分法2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        
        # 辅助函数：寻找第 k 小的元素
        def get_kth(k: int) -> int:
            idx1, idx2 = 0, 0
            while True:
                # 1. 边界情况处理
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])
                
                # 2. 确定比较位置（防止越界）
                # 我们想比较第 k/2 个元素，但如果数组不够长，就取最后一个
                step = k // 2
                new_idx1 = min(idx1 + step - 1, m - 1)
                new_idx2 = min(idx2 + step - 1, n - 1)
                
                val1, val2 = nums1[new_idx1], nums2[new_idx2]
                
                # 3. 核心排除逻辑
                if val1 <= val2:
                    # nums1 的前半部分太小了，不可能是第 k 小，排除掉
                    count_removed = new_idx1 - idx1 + 1
                    k -= count_removed
                    idx1 = new_idx1 + 1
                else:
                    # nums2 的前半部分太小了，排除掉
                    count_removed = new_idx2 - idx2 + 1
                    k -= count_removed
                    idx2 = new_idx2 + 1

        # 主逻辑
        if total % 2 == 1:
            # 奇数：直接找中间那个
            return float(get_kth((total + 1) // 2))
        else:
            # 偶数：找中间两个
            # 优化点：虽然调用了两次，但对于对数复杂度来说，常数级的重复是可以接受的
            # 如果要极致优化，可以修改 get_kth 一次返回两个值，但代码复杂度会上升，得不偿失
            left_val = get_kth(total // 2)
            right_val = get_kth(total // 2 + 1)
            return (left_val + right_val) / 2.0

# ## 二分法3


# class Solution:
#     def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
#         if len(a) > len(b):
#             a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

#         m, n = len(a), len(b)
#         a = [-inf] + a + [inf]
#         b = [-inf] + b + [inf]

#         # 枚举 nums1 有 i 个数在第一组
#         # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
#         i, j = 0, (m + n + 1) // 2
#         while True:
#             if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
#                 max1 = max(a[i], b[j])  # 第一组的最大值
#                 min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
#                 return max1 if (m + n) % 2 else (max1 + min2) / 2
#             i += 1  # 继续枚举
#             j -= 1


# from typing import List

# @lc code=end

