#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (36.06%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 87.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2: return False

        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        left = right = 0
        while right < l2:
            c2[s2[right]] += 1
            if c1 == c2: return True
            right += 1
            # 准备移动left，同时更新Window字典c2
            if right - left + 1 > l1:
                c2[s2[left]] -= 1
                if c2[s2[left]] == 0:
                    del c2[s2[left]]
                left += 1
        return False
# @lc code=end

