class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_ab_dict = {}
        sum_cd_dict = {}
        for a in A:
            for b in B:
                sum = a + b
                if sum not in sum_ab_dict:
                    sum_ab_dict[sum] = 1
                else:
                    sum_ab_dict[sum] += 1

        for c in C:
            for d in D:
                sum = c + d
                if -sum in sum_ab_dict:
                    if sum not in sum_cd_dict:
                        sum_cd_dict[sum] = 1
                    else:
                        sum_cd_dict[sum] += 1
        count = 0
        for i in sum_cd_dict:
            count +=sum_cd_dict[i]*sum_ab_dict[-i]
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount(A=[1,2],B=[-2,-1],C=[-1,2],D=[0,2]))