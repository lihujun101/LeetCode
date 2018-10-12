class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 由于是排好序的，可以这样做
        # 1、两个指针，一个在左边，一个在右边
        # 2、左+右> target ,右往左移动，左+右<target ,左往右移动
        # 3、直到找到值位置
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
if __name__ == '__main__':
    s= Solution()
    print(s.twoSum(numbers = [2, 7, 11, 15], target = 13))