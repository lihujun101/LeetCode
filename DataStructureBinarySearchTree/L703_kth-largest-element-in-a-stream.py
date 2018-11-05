'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.root = None
        for val in nums:
            self.root = self._insert_to_binary_search_tree(self.root, val)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.root = self._insert_to_binary_search_tree(self.root, val)
        return self._search_K_in_binart_search_tree(self.root, self.k)

    def _insert_to_binary_search_tree(self, root, val):
        if not root:
            root = TreeNode(val)
            return root
        if val > root.val:
            root.cnt += 1
            if root.right:
                self._insert_to_binary_search_tree(root.right, val)
            else:
                root.right = TreeNode(val)
        elif val < root.val:
            root.cnt += 1
            if root.left:
                self._insert_to_binary_search_tree(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            root.cnt += 1
        return root

    # 由于采用了递归，所以数据一旦超过900就会出现栈溢出！！！！，需要重新换方法
    def _search_K_in_binart_search_tree(self, root, k):

        # 先确定左，右子树的节点数
        right_cnt, left_cnt = 0, 0
        if root.right:
            right_cnt = root.right.cnt
        if root.left:
            left_cnt = root.left.cnt
        # root所在的排序范围
        root_idx_start = right_cnt + 1
        root_idx_end = right_cnt + (root.cnt - left_cnt - right_cnt)
        if root_idx_end < k:
            k = k - right_cnt - (root.cnt - left_cnt - right_cnt)
            return self._search_K_in_binart_search_tree(root.left, k)
        elif root_idx_start > k:
            return self._search_K_in_binart_search_tree(root.right, k)
        else:
            return root.val

'''

# 采用最小堆排序
import heapq


# 也就是始终保持只有K个数字
class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)  # 返回最大值堆顶线性将list转为堆结构
        while len(self.nums) > k:
            heapq.heappop(self.nums)  # 弹出最小值，直到最小值为第K大的数停止

    def add(self, val):
        if len(self.nums) < self.k:# add的时候检查，如果nums的长度小于k的话就推入一个值，主要的可能情况就是原来nums =[]
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:  # 如果val的值大于最小值的话，则删除最小值，并重新推一个值进去
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


if __name__ == '__main__':
    k = 1
    nums = []
    for n in range(800):
        nums.append(n)
        # nums = [5, 2, 6, 1, 7, 4, 3, 5, 2, 6, 1, 7, 4]
    s = KthLargest(k, nums)
    m = s.add(1)
    print(m)
