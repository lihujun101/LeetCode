class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 还有一种做法，s和t各一个指针，并结合字典
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        char_dict1 = {}
        char_dict2 = {}
        s1,t1 = "" ,""
        for i in range(len(s)):
            char_dict1[s[i]] = t[i]
            char_dict2[t[i]] = s[i]
        for i in range(len(s)):
            s1 += char_dict1[s[i]]
        for i in range(len(s)):
            t1 += char_dict2[t[i]]
        return s1==t and t1 == s


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic(s="aa", t="bb"))
