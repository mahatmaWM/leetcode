#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#
# https://leetcode-cn.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (60.54%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 27.7K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
#
# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
#
#
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
#
#
#
# 示例：
#
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
#
#
#
# 提示：
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
#


# @lc code=start
class Solution:
    # 模拟过程，每次取最大的两个元素操作，利用堆
    # 也可以排序后，取出最大的两个元素碰撞，然后使用bisect二分查找的方式插入剩余有序数组
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python只有最小堆，所以每个石头的重量取负号存入
        stones = [-x for x in stones]
        import heapq
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            heapq.heappush(stones, -abs(x - y))
        return -stones[0]

# @lc code=end
