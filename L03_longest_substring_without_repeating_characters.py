class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ""
        container = set()

        if s == "":
            return 0
        for i in range(len(s)):
            if string != "":
                for j in range(len(string)):
                    if s[i] == string[j]:
                        container.add(string)
                        if j != len(string) - 1:
                            string = string[j + 1:]
                        else:
                            string = ""
                        break
            string = string + s[i]
            if i == len(s) - 1:
                container.add(string)
        length = 0
        while container and len(container) != 0:
            longstring = len(container.pop())
            if longstring > length:
                length = longstring
        # print(container)
        return (length)