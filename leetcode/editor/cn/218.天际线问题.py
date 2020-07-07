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
class Node:
    def __init__(self, startIndex, endIndex, val):
        self.start = startIndex
        self.end = endIndex
        self.val = val
        # lazy更新法
        self.lazyVal = None
        self.left = None
        self.right = None

class MultiOverwriteSegmentTree:
    def __init__(self, data):
        self.data = data
        self.root = self._buildTree(0, len(self.data)-1)

    def _buildTree(self, start, end):
        if start == end:
            return Node(start, end, self.data[start])

        root = Node(start, end, 0)
        mid = (start + end) // 2
        root.left = self._buildTree(start, mid)
        root.right = self._buildTree(mid+1, end)
        root.val = max(root.left.val, root.right.val)
        return root

    def updateRange(self, i, j, val):
        self._updateRange(self.root, i, j, val)

    def _updateRange(self, root, i, j, val):
        start, end = root.start, root.end
        if i == start and j == end:
            root.val = val
            root.lazyVal = val
            return

        # 当node的lazyVal不为空的时候，需要将缓存的lazy值下推给子node
        if root.lazyVal is not None:
            self._pushDown(root)

        mid = (start + end) // 2
        if j <= mid:
            self._updateRange(root.left, i, j, val)
        elif i >= mid+1:
            self._updateRange(root.right, i, j, val)
        else:
            self._updateRange(root.left, i, mid, val)
            self._updateRange(root.right, mid+1, j, val)

    def getRange(self, i, j):
        return self._getRange(self.root, i, j)

    def _getRange(self, root, i, j):
        start, end = root.start, root.end
        if i == start and j == end:
            return root.val

        # 当node的lazyVal不为空的时候，需要将缓存的lazy值下推给子node
        if root.lazyVal is not None:
            self._pushDown(root)

        mid = (start + end) // 2
        if j <= mid:
            return self._getRange(root.left, i, j)
        if i >= mid+1:
            return self._getRange(root.right, i, j)
        return max(self._getRange(root.left, i, mid), self._getRange(root.right, mid+1, j))

    def _pushDown(self, root):
        if root.left:
            root.left.val = root.lazyVal
            root.left.lazyVal = root.lazyVal
        if root.right:
            root.right.val = root.lazyVal
            root.right.lazyVal = root.lazyVal
        root.lazyVal = None

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
# @lc code=end

