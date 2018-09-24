# class Solution:
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         length = len(nums)
#         begin, end = 0, length - 1
#         # 返回第一个值的位置
#         ranking_sort_num = length - k
#         p = self.partition(nums, begin, end)
#         while True:
#             if p < ranking_sort_num:
#                 p = self.partition(nums, p + 1, end)
#             elif p > ranking_sort_num:
#                 p = self.partition(nums, begin, p - 1)
#             else:
#                 return nums[p]
#
#     def partition(self, seq, begin, end):
#
#         if len(seq) == 1:
#             return 0
#         if len(seq) == 0:
#             return
#         p = begin
#         l = begin
#         r = end
#         while True:
#             while seq[l] <= seq[p] and l < r:
#                 l += 1
#             while seq[r] >= seq[p] and l <= r:
#                 r -= 1
#             if r <= l:
#                 break
#             else:
#                 seq[l], seq[r] = seq[r], seq[l]
#         seq[r], seq[p] = seq[p], seq[r]
#         return r


# 这个方法有点不合适！太取巧了，因为Python内置的排序是最快的，是快排的改良版
# class Solution:
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         seq = sorted(nums)
#         return seq[len(nums) - k]

# 使用heapq实现，时间复杂度 O(n*lgn)
# import heapq
# class Solution:
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heapq.heapify(nums)
#         return heapq.nlargest(k,nums)[-1]


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        pivot = nums[int(len(nums)/2)] # 避免出现部分有序的，每次都从中间取值
        less, greater = [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:  # 不含等于，等于可能会出现死循环
                greater.append(num)
        if k <= len(greater):  # 如果k <= greater的长度,那k大就在greater里面寻找
            return self.findKthLargest(greater, k)
        elif k > len(nums) - len(less): # 去less里找，但是k的值需要调整成在k的位置
            return self.findKthLargest(less, k - (len(nums)-len(less)))
        else:
            return pivot


if __name__ == '__main__':
    s = Solution()
    l = [12,2,3,5]
    print(s.findKthLargest(l, 4))
