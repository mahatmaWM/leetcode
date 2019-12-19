# 假设有打乱顺序的一群人站成一个队列。
# 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意： 
# 总人数少于1100人。
#
# 示例 
#
# 
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# Related Topics 贪心算法

# 贪心思路：高个子先站好位，矮个子插入到K位置上，前面肯定有K个高个子，矮个子再插到前面也满足K的要求

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照身高降序排，身高相同则按前面人数的多少升序排
        people.sort(key=lambda x: [-x[0], x[1]])
        # print(people)
        res = []
        # 遍历排序后的数组，根据K插入到K的位置上
        for p in people:
            res.insert(p[1], p)
        return res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().reconstructQueue(
        people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
