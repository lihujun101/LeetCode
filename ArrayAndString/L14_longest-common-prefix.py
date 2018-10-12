class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 遍历一次即可，先比较strs[0],strs[1]中的最长子串str，然后str和str[2]比较找到最长子串

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        same_string = strs[0]
        if same_string == "":
            return ""
        for idx in range(1, len(strs)):
            if strs[idx] == "":
                return ""
            if same_string[0] == strs[idx][0]:
                compared_str = strs[idx]
                i, j = 0, 0
                while (i <= len(same_string) - 1 and j <= len(compared_str) - 1):
                    if same_string[i] == compared_str[j]:
                        i += 1
                        j += 1
                    else:
                        break

                same_string = same_string[0:i]

            else:
                return ""
        return same_string


if __name__ == '__main__':
    strs =["a",'a']
    s = Solution()
    print(s.longestCommonPrefix(strs))
