class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        node_label = node.label
        node_copy = UndirectedGraphNode(node_label)
        if not node.neighbors:
            return node_copy

    searched = set()
    def _node_copy(self,node):
        node0 = UndirectedGraphNode(node.label)

        for neighbor in node.neighbors:
            if neighbor not in self.searched:
                self.searched.add(neighbor)
                neighbor_copy = self._node_copy(neighbor)
                node1 = UndirectedGraphNode(neighbor_copy.label)
                node0.neighbors.append(node1)
        return node0








if __name__ == '__main__':
    node_0 = UndirectedGraphNode(0)
    node_1 = UndirectedGraphNode(1)
    node_2 = UndirectedGraphNode(2)
    node_0.neighbors = [node_1, node_2]
    node_1.neighbors = [node_0, node_2]
    node_2.neighbors = [node_0, node_1, node_2]
    s = Solution()
    node4 = s._node_copy(node_0)
    print(node4)
