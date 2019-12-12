# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。 
#
# 示例: 
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# Related Topics 并查集 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 保存子节点 与 父节点 的关系
        union_find = dict([(item, item) for item in nums])
        # 这里是进行合并
        for item in nums:
            # 这个数组主要是为了在查找记录下查找路径，然后找到最终的父节点， 其实也就是路径压缩
            need_mod = [item]
            # 这里的 item+1 和下面的parent + 1 都是为了 和一些单独的点进行合并
            parent = item + 1
            # 下面的这个 默认横线是防止序列中有 0 出现
            pv = union_find.get(parent, "-")

            # 当这个点和父节点一样的时候表示的就是还没进行过筛选 或者就是本身自己一个集合
            # 当这个点的父节点和当前点不一样的时候有两种情况 要么是没有记录 要么是之前已经找到过了它最终父节点，也就是找到了它所属集合
            while pv == parent:
                need_mod.append(parent)
                parent += 1
                pv = union_find.get(parent, "-")

            if pv == "-":
                parent -= 1
            else:
                parent = pv
            # 统一设置一下他们的父节点 也就是路径压缩
            for tmp in need_mod:
                union_find[tmp] = parent
        # 这里是合并

        _min = -0xfffffff
        cm = _min
        cn = {}
        # 这里是获取父节点最多出现的次数，和并查集没毛关系
        for item in union_find:
            k = union_find.get(item)
            if not cn.get(k):
                cn[k] = 1
            else:
                cn[k] += 1
            cm = max(cm, cn[k])
        # 这里是获取父节点最多出现的次数，和并查集没毛关系

        return max(cm, 0)  # 这里主要是为了防止空列表的出现

# leetcode submit region end(Prohibit modification and deletion)
