
# 两者的区别和联系

两者的区别和联系如下：
1.两者在复杂度上同级, 但是树状数组的常数明显优于线段树, 其编程复杂度也远小于线段树.
2.树状数组的作用被线段树完全涵盖, 凡是可以使用树状数组解决的问题, 使用线段树一定可以解决, 但是线段树能够解决的问题树状数组未必能够解决.
3.树状数组的突出特点是其编程的极端简洁性, 使用lowbit技术可以在很短的几步操作中完成树状数组的核心操作，其代码效率远高于线段树。

# 树状数组
[树状数组BIT视频讲解](https://www.youtube.com/watch?v=WbafSgetDDk&pbjreload=101)

```python
class BinaryIndexedTree(object):
    # 注意index从1开始到N
    def __init__(self, N):
        self.BIT = [0] * (N + 1)

    def __low_bit(self, x):
        return x & (-x)

    # 第index个节点增加delta, index从1开始算起
    def update(self, index, delta):
        while index < len(self.BIT):
            self.BIT[index] += delta
            index += self.__low_bit(index)

    # 求数组A[1..index]的和, 包含index
    def get_sum(self, index):
        ans = 0
        while index > 0:
            ans += self.BIT[index]
            index -= self.__low_bit(index)
        return ans
```

# 线段树
[线段树视频讲解](https://www.youtube.com/watch?v=rYBtViWXYeI)
## 线段树定义
线段树（segment tree），用来存放给定区间（segment, or interval）内对应信息的一种数据结构。
树状数组（binary indexed tree）相似，线段树也用来处理数组相应的区间查询（range query）和元素更新（update）操作。
与树状数组不同的是，线段树不止可以适用于**区间求和**的查询，也可以进行**区间最大值，区间最小值，区间异或值**的查询，具体的用途涉及到线段树节点的设计，下文代码例子以307题区间求和举例。
和树状数组一样，线段树进行更新（update）的操作为O(logn)，进行区间查询（range query）的操作也为O(logn)