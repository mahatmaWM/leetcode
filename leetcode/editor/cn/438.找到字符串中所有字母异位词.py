#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (44.39%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 63.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#

# @lc code=start
class Solution:
    # 思路：和76题类似
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}
        p_counts = {}
        for c in p:
            p_counts[c] = p_counts.get(c, 0) + 1

        left = right = 0
        while right < len(s):
            c = s[right]
            # 遇到不需要的字符，则清空之前window以及同时移动left right指针
            if c not in p_counts:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1
                # 如果找到一个候选解，则看是否满足条件，且完了要右移left指针
                if right - left + 1 == len(p):
                    if window == p_counts: res.append(left)
                    window[s[left]] -= 1
                    left += 1
                # right右移
                right += 1
        return res

# @lc code=end

