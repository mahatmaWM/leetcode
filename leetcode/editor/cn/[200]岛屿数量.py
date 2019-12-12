# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
# 一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
# 你可以假设网格的四个边均被水包围。
#
# 示例 1: 
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
# 
#
# 示例 2: 
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
# 
# Related Topics 深度优先搜索 广度优先搜索 并查集

# 思路一，flood fill方法的深度优先搜索版本。


# 思路二，flood fill方法的广度优先搜索版本。
# class Solution:
#     #        x-1,y
#     # x,y-1    x,y      x,y+1
#     #        x+1,y
#     # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
#     directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#
#     def numIslands(self, grid):
#         m = len(grid)
#         # 特判
#         if m == 0:
#             return 0
#         n = len(grid[0])
#         marked = [[False for _ in range(n)] for _ in range(m)]
#         count = 0
#         # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
#         for i in range(m):
#             for j in range(n):
#                 # 只要是陆地，且没有被访问过的，就可以使用 BFS 发现与之相连的陆地，并进行标记
#                 if not marked[i][j] and grid[i][j] == '1':
#                     # count 可以理解为连通分量，你可以在广度优先遍历完成以后，再计数，
#                     # 即这行代码放在【位置 1】也是可以的
#                     count += 1
#                     queue = deque()
#                     queue.append((i, j))
#                     # 注意：这里要标记上已经访问过
#                     marked[i][j] = True
#                     while queue:
#                         cur_x, cur_y = queue.popleft()
#                         # 得到 4 个方向的坐标
#                         for direction in self.directions:
#                             new_i = cur_x + direction[0]
#                             new_j = cur_y + direction[1]
#                             # 如果不越界、没有被访问过、并且还要是陆地，我就继续放入队列，放入队列的同时，要记得标记已经访问过
#                             if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
#                                 queue.append((new_i, new_j))
#                                 #【特别注意】在放入队列以后，要马上标记成已经访问过，语义也是十分清楚的：反正只要进入了队列，你迟早都会遍历到它
#                                 # 而不是在出队列的时候再标记
#                                 #【特别注意】如果是出队列的时候再标记，会造成很多重复的结点进入队列，造成重复的操作，这句话如果你没有写对地方，代码会严重超时的
#                                 marked[new_i][new_j] = True
#                     #【位置 1】
#         return count


# 思路三，使用并查集求解，关于并查集的介绍https://www.jianshu.com/p/89cea54d3f22
# class Solution:
#     def numIslands(self, grid):
#
#         class UnionFind:
#
#             def __init__(self, n):
#                 self.count = n
#                 self.parent = [i for i in range(n)]
#                 self.rank = [1 for _ in range(n)]
#
#             def get_count(self):
#                 return self.count
#
#             def find(self, p):
#                 while p != self.parent[p]:
#                     self.parent[p] = self.parent[self.parent[p]]
#                     p = self.parent[p]
#                 return p
#
#             def is_connected(self, p, q):
#                 return self.find(p) == self.find(q)
#
#             def union(self, p, q):
#                 p_root = self.find(p)
#                 q_root = self.find(q)
#                 if p_root == q_root:
#                     return
#
#                 if self.rank[p_root] > self.rank[q_root]:
#                     self.parent[q_root] = p_root
#                 elif self.rank[p_root] < self.rank[q_root]:
#                     self.parent[p_root] = q_root
#                 else:
#                     self.parent[q_root] = p_root
#                     self.rank[p_root] += 1
#
#                 self.count -= 1
#
#         row = len(grid)
#         # 特判
#         if row == 0:
#             return 0
#         col = len(grid[0])
#
#         # 把二维坐标转化成并查集中的一维点
#         def get_index(x, y):
#             return x * col + y
#
#         # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
#         directions = [(1, 0), (0, 1)]
#         # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
#         dummy_node = row * col
#
#         # 多开的一个空间就是那个虚拟的空间
#         uf = UnionFind(dummy_node + 1)
#         for i in range(row):
#             for j in range(col):
#                 # 如果是水域，都连到那个虚拟的空间去
#                 if grid[i][j] == '0':
#                     uf.union(get_index(i, j), dummy_node)
#                 if grid[i][j] == '1':
#                     # 向下向右如果都是陆地，即 "1"，就要合并一下
#                     for direction in directions:
#                         new_x = i + direction[0]
#                         new_y = j + direction[1]
#                         if new_x < row and new_y < col and grid[new_x][new_y] == '1':
#                             uf.union(get_index(i, j), get_index(new_x, new_y))
#         # 不要忘记把那个虚拟结点减掉
#         return uf.get_count() - 1

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，也可以在dfs遍历之前计数
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and \
                    not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)

# leetcode submit region end(Prohibit modification and deletion)
