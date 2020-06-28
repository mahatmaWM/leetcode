#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (49.57%)
# Likes:    606
# Dislikes: 0
# Total Accepted:    116.6K
# Total Submissions: 235.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class UnionFind:

            def __init__(self, n):
                # 记录有多少个连通分量
                self.count = n
                # 记录每个节点的父亲节点
                self.parent = [i for i in range(n)]
                # 新增一个数组记录树的“重量”
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    # 进行路径压缩
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return
                # 小树接到大树下面较平衡
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += self.rank[q_root]
                else:
                    self.parent[p_root] = q_root
                    self.rank[q_root] += self.rank[p_root]
                self.count -= 1

        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])

        # 把二维坐标转化成并查集中的一维点
        def get_index(x, y):
            return x * col + y

        # 注意：因为row和col是递增遍历，我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = row * col

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1


# flood fill方法的深度优先搜索版本
class Solution1(object):
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])

        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 发现一个新陆地
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)

# flood fill方法的广度优先搜索版本
class Solution2:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 BFS 操作
        for i in range(m):
            for j in range(n):
                # 新陆地
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))

                    # 这里要标记上已经访问过
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                #【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
                                # 而不是在出队列的时候再标记
                                #【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
                                marked[new_i][new_j] = True
        return count
# @lc code=end
