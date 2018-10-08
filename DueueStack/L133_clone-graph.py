class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, node):
        '''
        :param node: UndirectedGraphNode
        :return node: UndirectedGraphNode
        '''

        if node is None:
            return
        new_node_dict = dict()
        # 1、先将所有的节点找到
        # 2、并生成一个字典，字典中关系是{old_node:copy_node}

        for nd in self._get_nodes(node):
            new_node = UndirectedGraphNode(nd.label)
            new_node_dict[nd] = new_node

        # 3、通过字典映射，将新节点进行联系
        for nd in self._get_nodes(node):
            for nd_nei in nd.neighbors:
                new_node_dict[nd].neighbors.append(new_node_dict[nd_nei])
        return new_node_dict[node]

    def _get_nodes(self, node):
        s = set()
        neighbors = node.neighbors
        s.add(node)
        while neighbors:
            nei = neighbors[-1]
            neighbors = neighbors[0:-1]
            temp = []
            if nei not in s:
                s.add(nei)
                temp += nei.neighbors
            if neighbors == []:
                neighbors = temp
        return s

    def cloneGraph2(self, node):
        # 优化后的方案
        if not node:
            return
        # 1、初始化栈，生成一个新节点，并建立新老节点的关系
        stack = [node]
        new_node = UndirectedGraphNode(node.label)
        old_new_dict = {node: new_node}

        # 2、stack使用BFS搜索，每找到一个新节点，就加入至stack中，且生成新节点
        # 3、并生成老节点和新节点的映射关系
        # 4、找到新节点的邻居节点们，并建立邻居关系
        while stack:
            u = stack.pop()
            uneighbor = []
            for v in u.neighbors:
                if v not in old_new_dict:
                    stack.append(v)
                    nv = UndirectedGraphNode(v.label)
                    old_new_dict[v] = nv
                uneighbor.append(old_new_dict[v])
            old_new_dict[u].neighbors = uneighbor
        return new_node



if __name__ == '__main__':
    node_0 = UndirectedGraphNode(0)
    node_1 = UndirectedGraphNode(1)
    node_2 = UndirectedGraphNode(2)
    node_3 = UndirectedGraphNode(3)
    node_0.neighbors = [node_1, node_2]
    node_1.neighbors = [node_0, node_2, node_3]
    node_2.neighbors = [node_0, node_1, node_2]
    node_3.neighbors = [node_1]
    s = Solution()
    node4 = s.cloneGraph2(node_0)
    print(node4)
