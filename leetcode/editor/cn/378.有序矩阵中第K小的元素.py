# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
#
# 示例: 
#
# 
# matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
# 
#
# 说明: 
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
# Related Topics 堆 二分查找

# 思路1：堆
# 相当于N（行）个有序列中查找第K小元素，维护一个大小为N的堆来决定每次应该从哪个序列中获取元素，堆里保存(num, row, col)元组。
# 复杂度 有序列表建堆是O(min(k,N)) + k*O(log(min(k,N)))，实现见kthSmallest1

# 思路2：二分查找 NlogN
# 特点：这里粗看和74题类似，但是74是Z字形严格有序，这题不一定，所以不能按展开成一维有序，照位置索引二分查找元素的思路做。
# 常见的二分查找是在有序列中，二分索引的办法来查找元素，这里是采用二分begin end元素值的方法来查找，类似二分猜数字。见kthSmallest

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 先从右上角点出发，根据m[i][j]与target的大小关系，决定是下移动一行还是左移动一列，O(N)
        def count_smaller_equal_than_target(target, right_up_i, right_up_j):
            row, col = right_up_i, right_up_j
            counter = 0
            while col >= 0 and row <= right_up_j:
                if matrix[row][col] <= target:
                    counter += col + 1
                    row += 1
                else:
                    col -= 1
            return counter

        # 不断的二分更新low high之间的数字，然后去二维数组中查找小于等于此数字的个数，
        # 注意这里必须要等于（因为此数字可能不存在）
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low < high:
            mid = low + (high - low) // 2
            c = count_smaller_equal_than_target(mid, 0, n - 1)
            # print(low, high, mid, c)
            if c < k:  # 包含相等的数量小于k，才将中间值加1
                low = mid + 1
            else:
                high = mid
        return high

    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        minheap = []
        n = len(matrix)
        # 当k小于n时，只需遍历前k行
        for i in range(min(k, n)):
            heapq.heappush(minheap, (matrix[i][0], i, 0))

        counter = 0
        x, i, j = 0, 0, 0
        while counter < k:
            counter += 1
            x, i, j = heapq.heappop(minheap)
            if j < n - 1:
                # 向堆里加入该元素所在行的下一个元素
                heapq.heappush(minheap, (matrix[i][j + 1], i, j + 1))
        return x


# leetcode submit region end(Prohibit modification and deletion)
def main():
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]

    k = 8

    print(Solution().kthSmallest(matrix=matrix, k=k))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
