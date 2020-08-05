#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#
# https://leetcode-cn.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (44.85%)
# Likes:    78
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.7K
# Testcase Example:  '"H2O"'
#
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
#
# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
#
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2
# 这个表达是不可行的。
#
# 两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
#
# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
#
# 给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于
# 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。
#
# 示例 1:
#
#
# 输入:
# formula = "H2O"
# 输出: "H2O"
# 解释:
# 原子的数量是 {'H': 2, 'O': 1}。
#
#
# 示例 2:
#
#
# 输入:
# formula = "Mg(OH)2"
# 输出: "H2MgO2"
# 解释:
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#
#
# 示例 3:
#
#
# 输入:
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
# 解释:
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#
#
# 注意:
#
#
# 所有原子的第一个字母为大写，剩余字母都是小写。
# formula的长度在[1, 1000]之间。
# formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。
#
#
#

# @lc code=start
import collections


class Solution:
    # 和1106题类似
    def __init__(self) -> None:
        self.l = 0

    def countOfAtoms(self, formula: str) -> str:
        ans = ''
        items = self._countOfAtoms(formula).items()
        for k, v in sorted(items):
            ans += k
            if v > 1: ans += str(v)
        return ans

    # 有括号的嵌套定义使用递归最合适，递归处理一对（）* 括号以及括号后面的数字
    def _countOfAtoms(self, formula):
        cnt = collections.defaultdict(int)
        while self.l < len(formula):
            # 遇到（，开始一次递归，注意指针跳过（ 、 ）符号
            if formula[self.l] == '(':
                self.l += 1
                tmp_cnt = self._countOfAtoms(formula)
                self.l += 1
                tmp = self._getCount(formula)
                for k, v in tmp_cnt.items():
                    cnt[k] += v * tmp
            # 遇到），说明本轮处理完，return
            elif formula[self.l] == ')':
                return cnt
            # 否则正常的处理元素和次数
            else:
                name = self._getName(formula)
                cnt[name] += self._getCount(formula)
        return cnt

    # 获取元素名称
    def _getName(self, str):
        name = ''
        while self.l < len(str) and str[self.l].isalpha() and (name == '' or str[self.l].islower()):
            name += str[self.l]
            self.l += 1
        return name

    # 获取元素次数
    def _getCount(self, str):
        cnt = ''
        while self.l < len(str) and str[self.l].isdigit():
            cnt += str[self.l]
            self.l += 1
        return 1 if cnt == '' else int(cnt)


# @lc code=end

if __name__ == "__main__":
    print(Solution().countOfAtoms(formula='K4(ON(SO3)2)2'))
