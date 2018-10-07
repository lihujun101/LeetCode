class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 类似于最短路径问题，依然采用BFS
        if n < 2:
            return n
        sqrt_list = []
        i = 1
        while i ** 2 <= n:
            sqrt_list.append(i ** 2)
            i += 1
        toCheck = {n}
        cnt = 0
        while toCheck:
            cnt += 1
            temp = set()
            for i in toCheck:
                for j in sqrt_list:
                    if i == j:
                        return cnt
                    elif i < j:
                        break
                    else:
                        temp.add(i - j)
            toCheck = temp
        return cnt


if __name__ == '__main__':
    s = Solution()
    cnt = s.numSquares(12)
    print(cnt)
