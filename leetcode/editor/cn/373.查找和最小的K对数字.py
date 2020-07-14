#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
# https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (42.65%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 20.7K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
#
# 找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# 示例 3:
#
# 输入: nums1 = [1,2], nums2 = [3], k = 3
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#
#
#


# @lc code=start
class Solution:
    # 思路：最小堆，把所有的点对加入到最小堆，然后输出前k个。
    # 但没有利用到“两个数组都有序”这个条件，就算数组无序，也可以利用这个方法。
    #
    # 要利用有序这个条件，那么可以nums1 nums2逐次移动，贪心先找到k个元素。
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        queue = []
        if not nums1 or not nums2: return []
        # 堆中保存(两数字和，(i,j))
        heapq.heappush(queue, (nums1[0] + nums2[0], (0, 0)))
        # 防止重复加入
        visited = {(0, 0)}
        while queue and len(res) < k:
            _, (i, j) = heapq.heappop(queue)
            res.append((nums1[i], nums2[j]))

            # 移动nums1，加入堆
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            # 移动nums2，加入堆
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
        return res


# @lc code=end
