class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 时间复杂度为 O(log(m+n)),则一定是二分法
        #                 left_part | right_part
        # A[0], A[1], ..., A[i - 1] | A[i], A[i + 1], ..., A[m - 1]
        # B[0], B[1], ..., B[j - 1] | B[j], B[j + 1], ..., B[n - 1]

        # 1、len(left)==len(right)(或者len(left)+1==len(right))，即i+j = m-i+n-j
        # 2、A[i-1]<=B[j] && B[j-1]<=A[j]就满足条件了，如果B[j-1] > A[i]，则需A[i]增大，B[j-1]减小，j减小到0的时候，则B[j-1]没有left_B了
        # 3、中位数 = (max(A[i - 1],B[j-1]),min(A[i],A[j]))/2(或者mid = min(A[i],B[j]))
        # 4、其实并不是绝对的log(m+n)的方法，原解答也有问题，其实并不是log(m)的时间复杂度

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        if len(nums2) == 0:
            if len(nums1) % 2 != 0:
                return nums1[len(nums1) // 2]
            else:
                return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2

        j = len(nums2) // 2
        while True:
            i = (len(nums1) + len(nums2)) // 2 - j
            if j < len(nums2) and nums1[i - 1] > nums2[j]:
                j += 1
            elif j > 0 and nums2[j - 1] > nums1[i]:
                j -= 1
            else:
                # 确定左边最大值
                if j == 0:
                    max_left = nums1[i - 1]
                elif i == 0:
                    max_left = nums2[j - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if j == len(nums2):
                    min_right = nums1[i]
                elif i == len(nums1):
                    min_right = nums2[j]
                else:
                    min_right = min(nums1[i], nums2[j])

                # 长度之和为奇数的情况
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return min_right
                # 长度之和为偶数的情况
                else:
                    return (max_left + min_right) / 2


if __name__ == '__main__':
    nums2 = [1,2,2]
    nums1 = [1,2,3]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))
