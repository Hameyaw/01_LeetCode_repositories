#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#
### 方法一：滑动窗口 + 哈希表


# @lc code=start
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dic, res, i = {}, 0, -1
#         for j in range(len(s)):
#             if s[j] in dic:
#                 i =max(dic[s[j]], i) # 更新左指针 i
#             dic[s[j]] = j # 哈希表记录
#             res = max(res, j - i) # 更新结果
#         return res
        

### 方法二：动态规划 + 哈希表
# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取 s[j] 上次出现的位置索引 i
            dic[s[j]] = j # 哈希表记录 s[j] 最新出现的位置索引,更新哈希表
            tmp = tmp + 1 if tmp < j-i else j - i # 更新 tmp
            res = max(res, tmp) # 更新结果
        return res
    

# @lc code=end

