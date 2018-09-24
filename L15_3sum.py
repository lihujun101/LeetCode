from collections import Counter


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums_dict = Counter(nums)
        # nums_dict = dict()
        # nums_set = set(nums)
        # for num in nums_set:
        #     count = 0
        #     for num0 in nums:
        #         if num == num0:
        #             count += 1
        #     nums_dict[num] = count
        keys = list(nums_dict.keys())
        length_key = len(keys)
        nums_list = []
        print(keys)
        for key_idx in range(length_key):
            for key_idx_1 in range(key_idx + 1, length_key):
                for key_idx_2 in range(key_idx_1 + 1, length_key):
                    if keys[key_idx] == -(keys[key_idx_1] + keys[key_idx_2]):
                        nums_list.append([keys[key_idx], keys[key_idx_1], keys[key_idx_2]])

        for key_idx in range(length_key):
            for key_idx_1 in range(length_key):
                if keys[key_idx] == -2 * keys[key_idx_1] and nums_dict[keys[key_idx_1]] >= 2 and key_idx != key_idx_1:
                    nums_list.append([keys[key_idx_1], keys[key_idx_1], keys[key_idx]])

        if ((0 in keys) and nums_dict[0] >= 3):
            nums_list.append([0, 0, 0])
        return nums_list


if __name__ == '__main__':
    s = Solution()
    s1 = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(s1)
