#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (51.56%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    41.8K
# Total Submissions: 81K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#
#
#
# 提示：
#
#
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
#
#
#


# @lc code=start
class Solution:
    # 有向无环 DAG图才有拓扑排序。常用的方法：
    # 1、从 DAG 图中选择一个 没有前驱（入度为0）的顶点并输出。
    # 2、从图中删除该顶点和所有以它为起点的有向边。
    # 重复 1 和 2 直到当前的 DAG 图为空或当前图中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True

        # [0,1]表示先学习1，再学习0，注意：邻接表存放的是后继 successor 结点的集合
        in_degree = [0 for _ in range(numCourses)]
        adj_list = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            in_degree[second] += 1
            adj_list[first].add(second)

        # 所有入度为 0 的结点加入队列
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0: queue.append(i)

        # 从队列里面找入度为0的节点，不断更新后继节点的入度
        counter = 0
        while queue:
            top = queue.pop()
            counter += 1
            for successor in adj_list[top]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0: queue.append(successor)
        return counter == numCourses


# @lc code=end
