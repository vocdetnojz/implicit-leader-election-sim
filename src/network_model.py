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

    pass
