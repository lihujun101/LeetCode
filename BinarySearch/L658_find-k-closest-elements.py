class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 方法：
        # 1、如果x值在arr外，则取值就是arr前k个数或者arr后k个数
        # 2、如果x值在arr区间内，则先找到最接近x的值索引n，前后各取K个数，两个指针，一个指针指向n-k,一个指针指向n+k，
        #   此时理论长度为2k+1(若存在边界条件则长度小于这个值) ，时间复杂度O(logn)
        # 3、然后通过左右指针比较，左指针的差值大于右指针的差值时，左指针->，否则右指针 <-，直到right-left = k，时间复杂度 O(k)

        first_num = arr[0]
        last_num = arr[-1]
        # 大于最后一个值就是最后几个数
        # 小于第一个数就是前几个数
        if x >= last_num: return arr[-1 - k+1:]
        if x <= first_num: return arr[0:k]
        # 第2步骤
        left = 0
        right = len(arr) - 1
        location = - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid
            elif arr[mid] > x:
                right = mid
            else:
                location = mid
                break

        if location == -1:
            location = left if x - arr[left] < arr[right] - x else right

        # 第3步骤：
        left = location - k if location - k >= 0 else 0
        right = location + k if location + k <= len(arr) - 1 else len(arr) - 1
        while left + k < right:  # 当right-left = k停止
            if x - arr[left] > arr[right] - x:
                left += 1
            elif x - arr[left] <= arr[right] - x:
                right -= 1
        if x - arr[left] <= arr[right] - x:
            return arr[left:right]
        else:
            return arr[left + 1:right + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9))
