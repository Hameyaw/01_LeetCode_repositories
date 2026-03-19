#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return "" # 输入字符串为空时，返回空字符串

        start, end = 0, 0 # 记录最长回文子串的起始和结束位置

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i) # 以 s[i] 为中心的回文串长度
            len2 = self.expandAroundCenter(s, i, i + 1) # 以 s[i] 和 s[i + 1] 为中心的回文串长度
            max_len = max(len1, len2) # 当前中心扩展得到的最长回文串长度

            if max_len > end - start:  # 如果当前最长回文串长度大于之前记录的长度，更新起始和结束位置
                start = i - (max_len - 1) // 2 # 更新最长回文子串的起始位置
                end = i + max_len // 2 # 更新最长回文子串的结束位置

        return s[start:end + 1] # 返回最长回文子串
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 从中心向两边扩展，直到不满足回文条件
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1 # 返回回文串的长度，注意要减去多扩展的两次


## 官方解法01

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s
        
#         max_len = 1
#         begin = 0
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
        
#         # 递推开始
#         # 先枚举子串长度
#         for L in range(2, n + 1):
#             # 枚举左边界，左边界的上限设置可以宽松一些
#             for i in range(n):
#                 # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#                 j = L + i - 1
#                 # 如果右边界越界，就可以退出当前循环
#                 if j >= n:
#                     break
                    
#                 if s[i] != s[j]:
#                     dp[i][j] = False 
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
                
#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return s[begin:begin + max_len]


# @lc code=end

