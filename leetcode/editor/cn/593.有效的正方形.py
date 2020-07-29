#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#
# https://leetcode-cn.com/problems/valid-square/description/
#
# algorithms
# Medium (42.61%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 9.6K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# 给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
#
# 一个点的坐标（x，y）由一个有两个整数的整数数组表示。
#
# 示例:
#
#
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True
#
#
#
#
# 注意:
#
#
# 所有输入整数都在 [-10000，10000] 范围内。
# 一个有效的正方形有四个等长的正长和四个等角（90度角）。
# 输入点没有顺序。
#
#
#


# @lc code=start
class Solution:
    # 按照x坐标排序，排序后四条边p1p2，p2p4，p4p3 和 p3p1，对角线为 p1p4 和 p2p3
    # 如果4条边相等，对角线也相等即为正方形
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points.sort()
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]
        p4 = points[3]

        def dist(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        def fourLineEqual(s1, s2, s3, s4):
            if not any([s1, s2, s3, s4]):
                return False
            elif min([s1, s2, s3, s4]) == max([s1, s2, s3, s4]):
                return True
            else:
                return False

        if fourLineEqual(dist(p1, p2), dist(p2, p4), dist(p4, p3), dist(
                p3, p1)) and dist(p1, p4) == dist(p2, p3):
            return True
        return False


# @lc code=end
