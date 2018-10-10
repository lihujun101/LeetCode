class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # 依次拿钥匙开启房间，BFS
        # 1、去0号房间拿钥匙开启所有0号房间的钥匙所对应的门，如1，2号房间的门
        # 2、从1、2号房间拿钥匙去开启1、2号房间的钥匙所对应的门，依次内推，直到开启完成
        keys = set(rooms[0])
        opened = {0}
        while keys :
            key = keys.pop()
            if key not in opened:
                opened.add(key)
                for key_new in rooms[key]:
                    keys.add(key_new)

        return len(opened) == len(rooms)


if __name__ == '__main__':
    rooms =[[1,3],[3,0,1],[2],[0]]
    s = Solution()
    print(s.canVisitAllRooms(rooms))