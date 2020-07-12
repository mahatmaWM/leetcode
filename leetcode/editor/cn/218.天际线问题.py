#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
# https://leetcode-cn.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (42.33%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 18.5K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
#
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。
#
# ⁠
#
# 每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0
# ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0
# 的表面上的完美矩形。
#
# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
#
# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ]
# 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]
# ]。
#
# 说明:
#
#
# 任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
# 输入列表已经按左 x 坐标 Li  进行升序排列。
# 输出列表必须按 x 位排序。
# 输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
# 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
#
#
#

# @lc code=start
import heapq
class Solution:
    # https://leetcode-cn.com/problems/the-skyline-problem/solution/chu-xue-zhe-bu-yong-dui-yong-zi-dian-de-fang-fa-by/
    # Main idea：线性扫描每一个关键点,判断是左端点还是右端点
    # Steps: 1.初始化两个字典，一个字典用于记录右关键点，另一个用于记录答案。为什么用字典，因为对于每一个坐标x，应该只记录一个高度, i.e., 最高的。
    # 2.首先把每个关键点都记下来，简单明了，左端点标记left，右端点标记right，并按照左端点排序
    # 3. 初始化高度0，目前高度cur=0，开始扫描：
    # 如果这个点为左端点，把他我们把他右端点这样记录在字典里 dic[右端点]=高度：
    # 如果这个点的右端点已经在字典里，存入最高的。
    # 并检查字典的最高高度， 如果高度改变，说明这是一个天际线点，并把左端点和高度存入答案，如果已经被存入左端点，用最高高度覆盖
    # 如果这个点是右端点，把其对应高度值从字典里删掉，并检查高度是否改变，如果改变，把其和新的高度存入。 因为在存入右端点时已经检查过重复，所以不用再次检查。
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0: return []
        ans = {}
        height_dic = {}
        points = []
        # 初始化所有关键点
        for L, R, H in buildings:
            points.append((L, 'left', H, R))
            points.append((R, 'right', 0, 0))
        points.sort()
        height_dic[0] = 0
        cur = 0
        for x, s, H, R in points:
            # 这个关键点是左端
            if s == 'left':
                # 把其右端点和高度存入高度字典
                if R in height_dic.keys():
                    height_dic[R] = max(height_dic[R], H)
                else:
                    height_dic[R] = H
                # 当前的最高高度，如果其发生改变，则一定是天际线点
                new = max(height_dic.values())
                if new != cur:
                    if x in ans.keys():
                        ans[x] = max(ans[x], H)
                    else:
                        ans[x] = H
                    cur = new
            else:
                # 前面已经被删除了，所有没有，跳过
                if x not in height_dic.keys(): continue
                # 删除右端点及其高度，检查高度是否改变
                del height_dic[x]
                new = max(height_dic.values())
                if new != cur:
                    ans[x] = new
                    cur = new
        return [[k, v] for k, v in ans.items()]


class Solution2:
    # 分治法
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0: return []

        def merge(buildings, start, end):
            if start == end: return [[buildings[start][0], buildings[start][2]], [buildings[start][1], 0]]
            mid = (start + end) // 2
            skyline1 = merge(buildings, start, mid)
            skyline2 = merge(buildings, mid + 1, end)
            # 合并两组结果
            res = []
            h1, h2, i, j = 0, 0, 0, 0
            while i < len(skyline1) or j < len(skyline2):
                x1 = skyline1[i][0] if i < len(skyline1) else float('inf')
                x2 = skyline2[j][0] if j < len(skyline2) else float('inf')
                # 这里合并的几种情况
                x, h = 0, 0
                if x1 < x2:
                    h1, x, i = skyline1[i][1], x1, i + 1
                elif x1 > x2:
                    h2, x, j = skyline2[j][1], x2, j + 1
                elif x1 == x2:
                    h1, h2, x, i, j = skyline1[i][1], skyline2[j][1], x1, i + 1, j + 1
                h = max(h1, h2)
                if len(res) == 0 or h != res[-1][1]: res.append([x, h])
            return res

        return merge(buildings, 0, len(buildings) - 1)


# @lc code=end
