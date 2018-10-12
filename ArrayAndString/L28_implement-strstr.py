class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        idx_haystack = 0
        length_needle = len(needle)
        while idx_haystack <= len(haystack) - 1:
            if needle[0] == haystack[idx_haystack]:
                if length_needle > len(haystack[idx_haystack:]):
                    return -1
                compare_str = haystack[idx_haystack:length_needle + idx_haystack]
                if compare_str == needle:
                    return idx_haystack
            idx_haystack += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr( haystack = "mississippi", needle = "issip"))