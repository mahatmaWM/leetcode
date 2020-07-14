#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (38.01%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 43.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#
#
#

# @lc code=start
class Solution:
    # 递归 + 备忘录
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = collections.defaultdict(list)

        def dfs(s, start, word_dict):
            nonlocal memo
            if start in memo: return memo[start]
            res = list([])
            if start == len(s): res.append('')
            for end in range(start + 1, len(s) + 1):
                tmp_str = s[start:end]
                if tmp_str in word_dict:
                    right_res = dfs(s, end, word_dict)
                    for item in right_res:
                        res.append(tmp_str + ' ' + item)
            memo[start] = res
            return res

        res = dfs(s, 0, wordDict)
        return [item.rstrip() for item in res]
# @lc code=end

