class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_dict = dict()
        list2_dict = dict()
        for value, key in enumerate(list1):
            list1_dict[key] = value
        for value, key in enumerate(list2):
            if key in list1_dict:
                list2_dict[key] = value

        if not list2_dict:
            return []
        min = len(list1) + len(list2)
        keys = []
        for i in list2_dict:
            if min >= list1_dict[i] + list2_dict[i]:
                min = list1_dict[i] + list2_dict[i]

        for i in list2_dict:
            if min == list1_dict[i] + list2_dict[i]:
                keys.append(i)

        return keys


if __name__ == '__main__':
    s = Solution()
    list1 = ["vacag","KFC"]

    list2 = ["fvo","xrljq","jrl","KFC"]


    print(s.findRestaurant(list1, list2))
