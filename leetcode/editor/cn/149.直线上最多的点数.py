# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
#
# 示例 1: 
#
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
#
# 示例 2: 
#
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# Related Topics 哈希表 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)

        # 每个新节点都与已访问过的节点组成连线计算斜率，保存至lines
        lines, p_viz = {}, set()
        for i, (x, y) in enumerate(points):
            for (x_viz, y_viz, j) in p_viz:
                if x_viz != x:  # 求其y=kx+b的参数k, b
                    k = (y_viz - y) / (x_viz - x)
                    _k = (x_viz - x) / (y_viz - y) if y_viz != y else None
                    b = round(y - k * x, 6)  # 同样用来修正python的精度问题
                else:
                    k, _k, b = None, None, x
                # 将结点加入该参数确定的直线
                lines[(k, _k, b)] = lines.get((k, _k, b), set()) | \
                                    {(x, y, i), (x_viz, y_viz, j)}
            p_viz.add((x, y, i))
        return max(len(x) for x in lines.values())


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxPoints(points=[[3, 10], [0, 2], [0, 2], [3, 10]]))
