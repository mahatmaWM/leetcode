# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
#
# 说明: 
#
# 
# 单词是指由非空格字符组成的字符序列。 
# 每个单词的长度大于 0，小于等于 maxWidth。 
# 输入单词数组 words 至少包含一个单词。 
# 
#
# 示例: 
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 
#
# 示例 2: 
#
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
# 
#
# 示例 3: 
#
# 输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#  "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
# 
# Related Topics 字符串

# 先根据规则将每一行的单词存入列表
# 根据列表单词的数量放置空格：单词数为1和2时都比较简单，当单词数大于2时做额外处理（详情见代码）
# 最后处理最后一行，也比较简单


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        res = []
        l = 0
        s = []
        # 先将单词保存
        for i in range(len(words)):
            if l + len(words[i]) <= maxWidth:
                l = l + len(words[i]) + 1
                s.append(words[i])
            else:
                res.append(s)
                l = len(words[i]) + 1
                s = [words[i]]
        res.append(s)

        # 根据单词放空格
        ans = []
        for word in res[:-1]:
            if len(word) == 1:
                ans.append(word[0] + ' ' * (maxWidth - len(word[0])))
            elif len(word) == 2:
                ans.append(word[0] + ' ' * (
                        maxWidth - len(word[0]) - len(word[1])) +
                           word[1])
            else:  # 单词数大于2时
                sum1 = sum([len(i) for i in word])

                m = (maxWidth - sum1) // (len(word) - 1)
                n = (maxWidth - sum1) - m * (len(word) - 1)

                a = word[0]
                i = 1
                while i < len(word):
                    if n > 0:
                        a = a + ' ' * (m + 1) + word[i]
                    else:
                        a = a + ' ' * m + word[i]
                    i += 1
                    n -= 1
                ans.append(a)
        # 处理最后一行
        b = res[-1][0]
        i = 1
        while i < len(res[-1]):
            b = b + ' ' + res[-1][i]
            i += 1
        b += (maxWidth - len(b)) * ' '
        ans.append(b)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
