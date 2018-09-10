class Solution:
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, halflen = 0, m, (m + n + 1) / 2
        while True:
            i = int((imin + imax) / 2)
            j = int(halflen - i)
            if i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            elif i < m and B[j - 1] > A[i]:
                imin = i + 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1: # 避免后面出现out of range，点睛之笔
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    nums1 = []
    nums2 = [2]
    m = Solution()
    print(m.findMedianSortedArrays(nums1, nums2))
