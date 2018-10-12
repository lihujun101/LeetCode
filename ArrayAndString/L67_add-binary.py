class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a,2)+ int(b,2)
        return str(bin(c))[2:]

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("1010", "1011"))
