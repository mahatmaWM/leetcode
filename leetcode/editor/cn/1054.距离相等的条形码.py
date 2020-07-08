#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#
# https://leetcode-cn.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (34.21%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 12.7K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
#
# 请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#
#
#
# 示例 1：
#
# 输入：[1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
#
#
# 示例 2：
#
# 输入：[1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
#
#
#
# 提示：
#
#
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
#
#
#
#
#


# @lc code=start
class Solution:
    # 贪心，每次取出剩余数目最多的数（使用priority queue来保存）。
    # 模拟整个过程，注意如果从pq中取出的数字与目前res最后一位相同，则取pq中下一个数字，同时要更新val以及前一个pop入堆。
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        d = Counter(barcodes)
        # 根据出现次数构造pq
        import heapq
        pq = []
        for cur_key in d:
            heapq.heappush(pq, (-d[cur_key], cur_key))

        res = []
        while len(res) != len(barcodes):
            cur_times, cur_key = heapq.heappop(pq)
            # cur-key不适合，取next-key加入
            if res and cur_key == res[-1]:
                next_times, next_key = heapq.heappop(pq)
                res.append(next_key)
                heapq.heappush(pq, (next_times + 1, next_key))
                heapq.heappush(pq, (cur_times, cur_key))
            else:
                res.append(cur_key)
                heapq.heappush(pq, (cur_times + 1, cur_key))
        return res


# @lc code=end
