# -*- coding: utf-8 -*-
# Author:           Annihilation7
# Data:             2018-12-22  15:26
# Python version:   3.6

class Node:
    """节点类"""
    def __init__(self, is_word=False):
        self.is_Word = is_word  # 默认情况下self.is_Word为False
        self.next = dict()  # python是动态语言，无法指定类型，所以建立一个空字典就好了。
        # 小小的说明一下，正因为无法指定类型，我们可以向我们的Trie中添加不限于英文字符的任意字符！这就是python的牛逼之处呀，其他静态编译语言
        # 大多数都会写成：map<char, Node> 那么只能处理英文字符串了。。

class Trie:
    def __init__(self):
        self._root = Node()
        self._size = 0  # size初始化为零


    def isEmpty(self):
        return self._size == 0  # 判空


    def getSize(self):
        return self._size  # 获取树的size


    def contains(self, word):
        """
        判断单词word是否已经存在于树中(非递归版本)。
        Params:
            - word: 待查找单词
        """
        cur = self._root  # 从根节点开始
        for character in word:  # 遍历要查询的单词
            cur = cur.next.get(character, None)  # 找下一个节点中的字典以character为键所对应的值，没找到返回None
            if cur == None:
                return False  # 没找到返回False
        return cur.is_Word == True  # 即使找到最后了，也要注意那个"pan"和"panda"的问题哦，如果此时的is_Word为True，表明真的存在这个单词，否则还是不存在！


    def contains_RE(self, node, word, index):
        """
        判断单词word是否已经存在于树中(递归版本)。
        Params:
            - node: 当前节点
            - word: 待查找单词
            - index: 表明此时到达word的哪个element了，即word[index]是待考察的element。
        """
        if index == len(word):  # 递归到底的情况，同样要注意最后一个元素的is_Word是不是真的为True
            if node.is_Word:
                return True
            return False

        dst_element = word[index]  # 标记这个元素，方便大家理解后面的代码
        if node.next.get(dst_element, None) is None:  # 如果当前节点的next的dict键中不包含dst_element
            return False # 直接返回False
        return self.contains_RE(node.next[dst_element], word, index + 1) # 否则去到node的next中以dst_element为键的Node是否包含word[index + 1]


    def add(self, word):
        """
        向Trie中添加一个单词word，注意不是单个字符哦（课上讲的迭代版本）
        Params:
            - word: 待添加的单词
        """
        if self.contains(word):  # 先判断是否已经存在，存在直接返回就ok。
            return

        cur = self._root # 从根节点开始，前面也说过了，Trie的字符串全部是从根节点开始的哦
        for character in word:  # 遍历要添加的单词的element
            if cur.next.get(character, None) is None: # 如果next_node中以character为键的值不存在
                cur.next[character] = Node() # 就新建一个Node作为character的值
            cur = cur.next.get(character) # 更新cur到下一个以character为边的Node，注意代码的逻辑哦，值不存在就新建，此时也是到下一个character为边的Node
            # 只不过此时到达的是一个我们刚刚新建的空Node。如果存在，就直接到下一个已经存在的Node了，一点问题没有。

        cur.is_Word = True  # 最后注意既然是添加，所以单词尾部的element的is_Word一定要设为True，表示存在这个单词了。
        self._size += 1  # 更新self._size


    def add_RE(self, node, word, index):
        """
        向Trie中添加一个单词word（自己理解的递归版本）
        Params:
            - node: 当前节点
            - word: 待添加的单词
            - index: 表明此时到达word的哪个element了，即word[index]是待考察的element。
        """
        if index == len(word): # 递归到底的情况，注意可能涉及到更新当前节点的is_Word
            if not node.is_Word:   # 如果当前节点的is_Word为False
                node.is_Word = True # 更新为True
                self._size += 1  # 并维护self._size
            return

        dst_element = word[index] # 标记这个元素，方便理解后面的代码
        if node.next.get(dst_element, None) is None:  # 如果当前节点的next的dict键中不包含dst_element
            node.next[dst_element] = Node() # 就为这个键新建一个Node
        return self.add_RE(node.next[dst_element], word, index + 1)  # 新建了也好，没新建也罢，都是要跑到下一个节点去看word[index + 1]这个element
        # 是否存在，不存在就新建，存在就顺着往后撸。


    def isPrefix(self, astring):
        """
        查询是否在Trie中有单词以prefix为前缀，注意'abc'也是'abc'的前缀，另外递归版本的就不写了，甚至要比contains_RE简单
        Params:
            -astring: 待查询字符串
        Returns:
        有为True,没有返回False
        """
        cur = self._root
        for character in astring:
            cur = cur.next.get(character, None)
            if cur is None:
                return False
        return True  # 此时就不用考虑is_Word啦，因为只要找前缀，并非确认该前缀是否真正存在与trie中

    def remove(self, astring):
        """
        删除Trie树中的字符串。（自己的理解，有问题还请小伙伴指出，一般的竞赛神马的也不会涉及到删除操作的。）
        因为我们的Trie树只能从头往后撸，所以要先遍历一遍记录每个Node，然后反向遍历每个Node来从后往前删除，有点像单向链表哦。
        Params:
            - astring: 待删除的字符串
        """
        # 这里不调用self.contains判断astring是否存在于Trie中了，因为这样的话多了一次遍历。
        cur = self._root   # 从根节点出发，准备记录
        record = [cur]  # 初始化record，就是根节点
        # 因为如果你想删除'hello'，那么'h'的信息只有根节点有，所以根节点是必须要添加进record的。
        for character in astring:  #遍历astring
            flag = cur.next.get(character, None) # 判断Trie中到底有没有astring
            if flag is None:  # 如果没有，直接return就好。相比先contains判断的话少一次循环哦。
                return
            record.append(cur.next[character])  # 先将下一个Node添加进record中
            cur = cur.next[character]  # cur往后撸

        if len(cur.next):  # 这里是一种特殊情况：比如我们的Trie中有'pan'和'panda'，但是'panda'和'pan'有着共同的路径，即p->a->n，
            # 所以是不可能全部删除'p','a','n'的，因为'panda'我们并不想删除呀。
            # 这里的处理反倒很简单，直接将当前cur到达的node的is_Word设为False就好啦～，'pan'就不复存在了！
            cur.is_Word = False
            self._size -= 1  # 便忘了删完后维护一下self._size
            return

        # 删除操作
        string_index = len(astring) - 1 # 从后往前删，联想单链表删除操作
        for record_index in range(len(record) - 2, -1, -1):  # 此时record的容量应该为len(astring) + 1，因为我们一开始就添加了self._root
            # 而最后一个Node是没用的，因为要删除的话只能找到目标的前一个node进行删除，所以从倒数第二个node开始向前遍历
            remove_char = astring[string_index] # 记录要删除的字符，便与小伙伴理解
            cur_node = record[record_index] # 记录当前的node
            del cur_node.next[remove_char]  # 直接将当前node的next中以remove_char为键的 键值对 删除
            string_index -= 1  # 同步操作，维护一下string_index，准备删除下一个字符
        self._size -= 1  # 最后删完了别忘记维护一下self._size


    def printTrie(self):
        """打印Trie，为了debug用的。凑合看吧/(ㄒoㄒ)/~~前缀打印不出来--救我～"""
        def _printTrie(node):
            if not len(node.next): # 递归到底的情况，下面没Node了
                print('None')
                return

            for keys in node.next.keys(): # 对当前node的下面的每个character
                print(keys, end='->') # 打印character
                _printTrie(node.next[keys]) # 依次对下面的每个node都调用_printTrie方法来递归打印
        _printTrie(self._root)
