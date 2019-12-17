# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1: 
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
#
# 示例 2: 
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])

        tmp_inter = intervals[0]
        for i in range(1, len(intervals)):
            if tmp_inter[1] < intervals[i][0]:
                res.append(tmp_inter)
                tmp_inter = intervals[i]
            else:
                tmp_inter[1] = max(intervals[i][1], tmp_inter[1])
        res.append(tmp_inter)
        return res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
