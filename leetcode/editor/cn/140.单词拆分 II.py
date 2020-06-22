# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
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
#   "cats and dog",
#   "cat sand dog"
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
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
#
# 示例 3： 
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# Related Topics 动态规划 回溯算法

# 思路：标准的回溯解法（但是回溯会超时，需添加剪枝，太多状态都不合法）

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 这个回溯会超时，还没有想到怎么剪枝
    def wordBreak0(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.res = list([])
        length = set([len(w) for w in set(wordDict)])
        def backtrack(s, start, word_dict, tmp_list):
            if start == len(s):
                self.res.append(' '.join(tmp_list[:]))
            for end in range(start, len(s) + 1):
                if end-start not in length:
                    continue
                tmp_str = s[start:end]
                if tmp_str in word_dict:
                    tmp_list.append(tmp_str)
                    backtrack(s, end, word_dict, tmp_list)
                    tmp_list.pop()

        backtrack(s, 0, wordDict, [])
        return self.res

    # 递归写法
    def wordBreak1(self, s, wordDict):
        def dfs(s, start, word_dict):
            res = list([])
            if start == len(s):
                res.append('')
            for end in range(start + 1, len(s) + 1):
                tmp_str = s[start:end]
                if tmp_str in word_dict:
                    right_res = dfs(s, end, word_dict)
                    for item in right_res:
                        res.append(tmp_str + ' ' + item)
            return res

        res = dfs(s, 0, wordDict)
        return res

    # 递归 + 备忘录
    def wordBreak(self, s, wordDict):
        import collections
        self.memo = collections.defaultdict(list)

        def dfs(s, start, word_dict):
            if start in self.memo:
                return self.memo[start]
            res = list([])
            if start == len(s):
                res.append('')
            for end in range(start + 1, len(s) + 1):
                tmp_str = s[start:end]
                if tmp_str in word_dict:
                    right_res = dfs(s, end, word_dict)
                    for item in right_res:
                        res.append(tmp_str + ' ' + item)
            self.memo[start] = res
            return res

        res = dfs(s, 0, wordDict)
        # return res
        return [item.rstrip() for item in res]


# leetcode submit region end(Prohibit modification and deletion)
def main():
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine",
                "pineapple"]

    # s = 'a'
    # wordDict=['a']

    print(Solution().wordBreak(s=s, wordDict=wordDict))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
