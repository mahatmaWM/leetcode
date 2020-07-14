#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#
# https://leetcode-cn.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (36.44%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 7K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。
#
# 每个人都可能不喜欢其他人，那么他们不应该属于同一组。
#
# 形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。
#
# 当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。
#
#
#
#
#
#
# 示例 1：
#
# 输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
#
#
# 示例 2：
#
# 输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
#
#
# 示例 3：
#
# 输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# 对于dislikes[i] == dislikes[j] 不存在 i != j
#
#
#


# @lc code=start
class Solution:
    # 图标记两种颜色，bfs&dfs，785题类似，O(V+E)
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * N
        # 构造连接图
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        # dfs遍历图
        for i in range(len(graph)):
            if visited[i] == 1: continue
            color_map = {i + 1: 0}
            stack = [(i + 1, 0)]
            visited[i] = 1
            while stack:
                u, color = stack.pop(0)
                for v in graph[u]:
                    # 如果v没有被标过颜色
                    if v not in color_map:
                        color_map[v] = 1 - color
                        stack.append((v, 1 - color))
                        visited[v - 1] = 1
                    # 否则被标过颜色，就检查是否颜色冲突
                    elif color_map[v] == color_map[u]:
                        return False
        return True


# @lc code=end
