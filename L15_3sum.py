from time import time
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_list = []
        nums.sort()
        for i in range(len(nums) - 2):  #
            beg = i + 1
            end = len(nums) - 1
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            while beg < end:
                if nums[i] + nums[beg] + nums[end] == 0:
                    result_list.append([nums[i], nums[beg], nums[end]])
                    while nums[end - 1] == nums[end] and end - beg >= 2:
                        end -= 1
                    while nums[beg + 1] == nums[beg] and end - beg >= 2:
                        beg += 1
                    beg += 1
                    end -= 1
                elif nums[i] + nums[beg] + nums[end] > 0:
                    end -= 1
                else:
                    beg += 1
        return result_list




if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    # begin_t = time()
    # s = Solution1()
    # s2 = s.threeSum(nums)
    # end_t = time()
    # print(s2)
    # print(end_t - begin_t)

    s = Solution()
    begin_t = time()
    s1 = s.threeSum(nums)
    end_t = time()
    print(s1)
    print(end_t - begin_t)
