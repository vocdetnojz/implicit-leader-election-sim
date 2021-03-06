from node_model import NodeModel


class NetworkModel(object):
    """
    Network Model which contains the Nodes and the edges in between

    """

    def __init__(self, nodes, node_matrix):
        self.__nodes = nodes
        self.__node_matrix = node_matrix

    @property
    def size(self):
        return len(self.__nodes)

    @property
    def nodes(self):
        return self.__nodes

    @property
    def node_matrix(self):
        return self.__node_matrix

    @property
    def contenders(self):
        return [node for node in self.__nodes if node.is_contender]

    @property
    def proxies_ids(self):
        return [node.id for node in self.__nodes if node.get_contenders]

    def get_nodes_neighbors(self, node: NodeModel):
        ids = self.get_node_ids_neighbors(node.id)
        return [self.__nodes[n_id] for n_id in ids]

    def get_node_ids_neighbors(self, n_id):
        return self.__node_matrix.get_node_neighbor_ids(self.__nodes[n_id])

    pass
