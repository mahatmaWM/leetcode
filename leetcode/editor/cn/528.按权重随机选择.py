#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#
# https://leetcode-cn.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (43.43%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 6.6K
# Testcase Example:  '["Solution","pickIndex"]\r\n[[[1]],[]]\r'
#
# 给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与
# w[i] 成正比。
#
#
#
#
# 例如，给定一个值 [1，9] 的输入列表，当我们从中选择一个数字时，很有可能 10 次中有 9 次应该选择数字 9 作为答案。
#
#
#
# 示例 1：
#
# 输入：
# ["Solution","pickIndex"]
# [[[1]],[]]
# 输出：[null,0]
#
#
# 示例 2：
#
# 输入：
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# 输出：[null,0,1,1,1,0]
#
#
#
# 输入语法说明：
#
# 输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有一个参数，即数组 w。pickIndex
# 没有参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。
#
#
#
# 提示：
#
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex 将被调用不超过 10000 次
#
#
#


# @lc code=start
class Solution:
    # 根据权重w数组，将区间归一化为和为1的概率，然后依次计算cur_sum概率和
    # 随机返回概率时，看[0 1]之间的随机数落在什么区域，返回对应的概率值，使用二分查找
    def __init__(self, w: List[int]):
        self.probability = [0] * len(w)
        total_sum = sum(w)
        cur_sum = 0
        for i in range(len(w)):
            cur_sum += w[i]
            self.probability[i] = cur_sum / total_sum

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.probability, random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
