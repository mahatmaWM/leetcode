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
            # 记录当前遍历需要路径压缩的节点
            need_union = [item]

            # 尝试去找 item+1 节点的父亲
            # 由于外层有一个for循环，所以这里只需要找item+1即可（不用考虑item-1）
            try_node = item + 1
            try_node_parent = union_find.get(try_node, "-")

            # 当这个点和父节点一样的时候表示的就是还没进行过筛选 或者 就是本身自己一个集合
            # 当这个点的父节点和当前点不一样的时候有两种情况：
            #   1、要么是没有记录，则try_node-1
            #   2、要么是之前已经找到过了它最终父节点，也就是找到了它所属集合
            while try_node_parent == try_node:
                need_union.append(try_node)
                try_node += 1
                try_node_parent = union_find.get(try_node, "-")

            if try_node_parent == "-":
                try_node -= 1
            else:
                try_node = try_node_parent

            # 统一设置他们的父节点 也就是路径压缩
            for tmp in need_union:
                union_find[tmp] = try_node
            # print(union_find)

        # 父节点出现次数最多的
        import collections
        dict1 = collections.defaultdict(int)
        res = 0
        for k, v in union_find.items():
            dict1[v] += 1
        for k, v in dict1.items():
            res = max(res, v)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
