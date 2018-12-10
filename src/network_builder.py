import math
import random

from src.node_model import NodeModel
from src.node_matrix import NodeMatrix
from src.network_model import NetworkModel


class NetworkBuilder(object):

    def __init__(self, c1, c2, net_size, connectivity=1):
        self.__c1 = c1
        self.__c2 = c2
        self.__network_size = net_size
        self.__used_ids = list()  # not the part of the model, but will ensure that ids are not repeated
        self.__nodes = list()
        self.__node_matrix = NodeMatrix(self.__network_size)
        self.__connectivity = connectivity
        pass

    @property
    def nodes(self):
        return self.__nodes

    def build_network(self):
        for x in range(self.__network_size):
            self.__nodes.append(self.__gen_node_model(x))
            pass
        for i in range(self.__network_size):
            for j in range(i):
                if random.random() < self.__connectivity:
                    self.__node_matrix.make_edge(i, j)
                    self.__node_matrix.make_edge(j, i)
        return NetworkModel(self.__nodes, self.__node_matrix)

    def build_network_4_regular(self):
        """
        Main function of the network builder

        :return:
        """
        return self.__gen_network_model()

    def __gen_network_model(self):
        """
        Create a 4-regular super-node graph model based on size N

        :return:
        """
        for x in range(self.__network_size):
            self.__nodes.append(self.__gen_node_model(x))
            pass
        self.__node_matrix = NodeMatrix(self.__network_size)
        self.__gen_node_edges()
        return NetworkModel(self.__nodes, self.__node_matrix)

    def __gen_node_edges(self):
        """
        Generates node edges

        :return:
        """
        subgraph_nodes = []
        for i in range(len(self.__nodes) // 8):
            x = self.__nodes[i*8:i*8+8]
            subgraph_nodes.append(x)
            self.__gen_subgraph_edges(x)
        # connect subgraphs
        self.__subgraph_connector()
        return

    def __subgraph_connector(self):
        """
        Ugly connector between 8 pieces of 4-regular graphs with 8 nodes each

        :return:
        """
        self.__node_matrix.del_edge(0 * 8 + 2, 0 * 8 + 3)
        self.__node_matrix.del_edge(0 * 8 + 5, 0 * 8 + 6)
        self.__node_matrix.del_edge(1 * 8 + 2, 1 * 8 + 3)
        self.__node_matrix.del_edge(1 * 8 + 2, 1 * 8 + 3)
        self.__node_matrix.del_edge(2 * 8 + 2, 2 * 8 + 3)
        self.__node_matrix.del_edge(2 * 8 + 2, 2 * 8 + 3)
        self.__node_matrix.del_edge(3 * 8 + 2, 3 * 8 + 3)
        self.__node_matrix.del_edge(3 * 8 + 2, 3 * 8 + 3)
        self.__node_matrix.del_edge(4 * 8 + 2, 4 * 8 + 3)
        self.__node_matrix.del_edge(4 * 8 + 2, 4 * 8 + 3)
        self.__node_matrix.del_edge(5 * 8 + 2, 5 * 8 + 3)
        self.__node_matrix.del_edge(5 * 8 + 2, 5 * 8 + 3)
        self.__node_matrix.del_edge(6 * 8 + 2, 6 * 8 + 3)
        self.__node_matrix.del_edge(6 * 8 + 2, 6 * 8 + 3)
        self.__node_matrix.del_edge(7 * 8 + 2, 7 * 8 + 3)
        self.__node_matrix.del_edge(7 * 8 + 2, 7 * 8 + 3)
        self.__node_matrix.make_edge(0 * 8 + 2, 1 * 8 + 7)
        self.__node_matrix.make_edge(0 * 8 + 3, 3 * 8 + 0)
        self.__node_matrix.make_edge(0 * 8 + 5, 5 * 8 + 0)
        self.__node_matrix.make_edge(0 * 8 + 6, 7 * 8 + 1)
        self.__node_matrix.make_edge(1 * 8 + 3, 2 * 8 + 0)
        self.__node_matrix.make_edge(1 * 8 + 4, 4 * 8 + 1)
        self.__node_matrix.make_edge(1 * 8 + 6, 6 * 8 + 1)
        self.__node_matrix.make_edge(2 * 8 + 4, 3 * 8 + 1)
        self.__node_matrix.make_edge(2 * 8 + 5, 5 * 8 + 2)
        self.__node_matrix.make_edge(2 * 8 + 7, 7 * 8 + 2)
        self.__node_matrix.make_edge(3 * 8 + 5, 4 * 8 + 2)
        self.__node_matrix.make_edge(3 * 8 + 6, 6 * 8 + 3)
        self.__node_matrix.make_edge(4 * 8 + 6, 5 * 8 + 3)
        self.__node_matrix.make_edge(4 * 8 + 7, 7 * 8 + 4)
        self.__node_matrix.make_edge(5 * 8 + 7, 6 * 8 + 4)
        self.__node_matrix.make_edge(6 * 8 + 0, 7 * 8 + 5)
        pass

    def __gen_subgraph_edges(self, nodes: list):
        # nodes is assumed to be 8 long
        if not len(nodes) == 8:
            raise RuntimeError
        for i in range(len(nodes)):
            self.__node_matrix.make_edge(nodes[i], nodes[(i + 1) % len(nodes)])
            self.__node_matrix.make_edge(nodes[i], nodes[(i + 3) % len(nodes)])
            self.__node_matrix.make_edge(nodes[i], nodes[(i + 5) % len(nodes)])
            self.__node_matrix.make_edge(nodes[i], nodes[(i + 7) % len(nodes)])

    def __gen_node_model(self, id):
        """
        Generates a Node Model

        :return:
        """
        return NodeModel(id, self.__calc_contender_attr(), self.__c1, self.__c2)

    def __calc_contender_attr(self):
        """
        Calculate a boolean value for a node's contender attribute

        :return: boolean
        """
        return random.random() <= self.__c1 * math.log10(self.__network_size) / self.__network_size
