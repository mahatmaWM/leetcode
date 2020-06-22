# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明： 
#
# 
# 拆分时可以重复使用字典中的单词。 
# 你可以假设字典中没有重复的单词。 
# 
#
# 示例 1： 
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
#
# 示例 2： 
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 
#
# 示例 3： 
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# Related Topics 动态规划

# 时间复杂度：O(n^{2})

# 其实就是left right两个指针蛮力搜索字符串，当发现[left right]在字典中，且之前的切分合法，则right也可以作为一个切分点。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for left in range(n):
            if not dp[left]:
                continue
            for right in range(left + 1, n + 1):
                if dp[left] and s[left:right] in wordDict:
                    dp[right] = True
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
