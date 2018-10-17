class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        keys_dict = {}
        for string in strs:
            keys = [0 for i in range(ord('a'), ord('z') + 1)]
            for i in string:
                keys[ord(i) - 97] += 1
            keys_tuple = tuple(keys)

            if keys_tuple not in keys_dict:
                keys_dict[keys_tuple] = [string]
            else:
                keys_dict[keys_tuple].append(string)

        return (list(keys_dict.values()))


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(strs=[]))
