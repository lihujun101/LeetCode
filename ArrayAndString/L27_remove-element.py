class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 双指针l,r
        # 1、左边指针只要找到val就停下，然后右指针开始出发
        # 2、右指针只要找到的不是val就停下，
        # 3、然后左右指针找到的值交换，且左指针继续行进
        if len(nums) == 0:
            return 0

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] == val:
                exists = True
                if nums[r] != val:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                else:
                    r -= 1
            elif nums[l] != val:
                l += 1
        print(nums)
        return r + 1



if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums=[4,5], val=5))
