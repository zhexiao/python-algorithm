"""
二叉查找树（binary search tree）
定义：
1. 若左子树不空，则左子树上所有结点的值均小于或等于它的根结点的值。
2. 若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值。
3. 左、右子树也分别为二叉排序树。

最大值和最小值：
最左边的结点即为最小值，要查找最小值，仅仅需遍历左子树的结点直到为空为止。
最右边的结点结尾最大值，要查找最大值，仅仅需遍历右子树的结点直到为空为止。

查找与插入：
1. 首先将给定值与根结点的关键字比较，若相等，则查找成功
2. 若小于根结点的关键字值，递归查左子树
3. 若大于根结点的关键字值，递归查右子树
4. 若子树为空，查找不成功

删除，二叉查找树的删除操作分为三种情况（如图1）：
1. 如果待删除的节点是叶子节点，那么可以立即被删除
2. 如果节点只有一个儿子，则将此节点parent的指针指向此节点的儿子，然后删除节点
3. 如果节点有两个儿子，则将其右子树的最小数据代替此节点的数据，并将其右子树的最小数据删除

遍历
1. 先序遍历：访问根节点，遍历左子树，遍历右子树。
2. 中序遍历：遍历左子树，访问根节点，遍历右子树。
3. 后序遍历：遍历左子树，遍历右子树，访问根节点 。
"""


class TreeNode(object):
    """
    定义一个树节点
    """

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self, node_list):
        """
        实例化一棵树
        :param node_list: 列表
        """
        if not isinstance(node_list, list):
            raise Exception('参数为列表参数')

        # 定义一个根节点
        self.tree_root = TreeNode(node_list[0])

        # 把后面的值全部插入到树节点中
        for val in node_list[1:]:
            self.insert(val, self.tree_root)

    def insert(self, val, tree_node):
        """
        插入一个值到树中
        :param val:
        :param tree_node:
        :return:
        """
        # 找到了一个空位置
        if tree_node is None:
            tree_node = TreeNode(val)

        # 如果值大于树节点的值，则把这个值放在树节点的右边
        elif val > tree_node.data:
            tree_node.right_child = self.insert(val, tree_node.right_child)

        # 如果值小于树节点的值，则把这个值放在树节点的左边
        else:
            tree_node.left_child = self.insert(val, tree_node.left_child)

        return tree_node

    def search(self, val, tree_node):
        """
        搜索某个值
        :param val: 查找的值
        :param tree_node: 查找的树节点
        :return: 返回是否找到， 节点的父节点
        """
        # 如果节点不存在，肯定没找到
        if tree_node is None:
            return False

        # 如果值大于节点，则从节点右边继续找
        if val > tree_node.data:
            return self.search(val, tree_node.right_child)
        # 如果值小于节点，则从节点左边继续找
        elif val < tree_node.data:
            return self.search(val, tree_node.left_child)
        # 找到了
        else:
            return True

    def delete(self, val, tree_node):
        """
        删除二叉树中的val值
        :param val:
        :param tree_node:
        :return:
        """
        if tree_node is None:
            return

        if val > tree_node.data:
            tree_node.right_child = self.delete(val, tree_node.right_child)
        elif val < tree_node.data:
            tree_node.left_child = self.delete(val, tree_node.left_child)
        # 当val值等于节点值的时候，分为三种情况：
        # 有左右子树、只有左子树或者只有右子树、无左子树又无右子树
        else:
            # 既有左子节点又有右子节点
            if tree_node.left_child and tree_node.right_child:
                # 则需找到右子节点中最小节点
                right_min_node = self.find_min(tree_node.right_child)
                tree_node.data = right_min_node.data

                # 再把右子节点中的最小节点删除
                tree_node.right_child = self.delete(
                    right_min_node.data,
                    tree_node.right_child
                )
            # 左右子节点都为空
            elif tree_node.left_child is None and tree_node.right_child is None:
                tree_node = None
            # 只有右子节点
            elif tree_node.left_child is None:
                tree_node = tree_node.right_child
            # 只有左子节点
            elif tree_node.right_child is None:
                tree_node = tree_node.left_child

        return tree_node

    def find_min(self, tree_node):
        """
        找到最小值，从根节点开始，沿着左子树一直往下，直到找到最后一个左子树节点
        :param tree_node: 查找的树节点
        :return:
        """
        if tree_node.left_child:
            return self.find_min(tree_node.left_child)
        else:
            return tree_node

    def find_max(self, tree_node):
        """
        找到最大值，从根节点开始，沿着右子树一直往下，直到找到最后一个右子树节点
        :param tree_node:
        :return:
        """
        if tree_node.right_child:
            return self.find_max(tree_node.right_child)
        else:
            return tree_node

    def print_tree(self, tree_node):
        """
        打印二叉搜索树，中序打印
        :param tree_node:
        :return:
        """
        if tree_node is None:
            return

        self.print_tree(tree_node.left_child)
        print(tree_node.data, end=' ')
        self.print_tree(tree_node.right_child)


a = [17, 5, 35, 2, 11, 9, 16, 8, 29, 38]
# 创建二叉查找树
bst = BinarySearchTree(a)

print(bst.find_min(bst.tree_root).data)
print(bst.find_max(bst.tree_root).data)

bst.delete(11, bst.tree_root)
bst.print_tree(bst.tree_root)