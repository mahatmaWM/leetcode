# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为： 
#
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
# 
# Related Topics 字符串 回溯算法

# 根据解空间二叉树可知，如果左括号还有剩余，则可以放置左括号，如果右括号的剩余数大于左括号，则可以放置右括号。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.dfs(n, n, "")
        return self.res

    def dfs(self, left, right, cur_str):
        if left == 0 and right == 0:
            self.res.append(cur_str)
            return
        if left > 0:
            self.dfs(left - 1, right, cur_str + '(')
        if right > left and right > 0:
            self.dfs(left, right - 1, cur_str + ')')

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().generateParenthesis(n=3))
