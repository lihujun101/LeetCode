class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        count = 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
                count += 1
            else:
                nums_dict[num] += 1
        times_dict = {}

        for num in nums_dict:
            times = nums_dict[num]
            if times not in times_dict:
                times_dict[times] = {num}
            else:
                times_dict[times].add(num)
        #print(times_dict)
        times_s = sorted(times_dict)
        #print(times_s)
        sum = 0
        m = []
        for idx in range(len(times_s)-1, -1, -1):
            sum += len(times_dict[times_s[idx]])
            m += list(times_dict[times_s[idx]])
            if sum >= k :
                break
        return m



if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(nums= [1,1,1,2,2,3] , k=2))
