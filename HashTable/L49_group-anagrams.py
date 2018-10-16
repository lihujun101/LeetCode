class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        for string in strs:
            dict = {}
            for i in string:
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i]
