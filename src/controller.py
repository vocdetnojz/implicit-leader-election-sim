import random
from src.node_model import NodeModel
from src.network_builder import NetworkBuilder


class Controller(object):

    def __init__(self, network_size: int = 10):
        self.__pref_network_size = network_size
        self.__network = NetworkBuilder().build_network()
        pass

    def run(self):
        # TODO
        pass

    def __init_random_walk_phase(self):
        """
        Algorithm 1 Step 3
        Each contender begins the protocol by executing a Random Walk Phase of length O(1)

        :return:
        """
        for contender in self.__network.contenders:
            p = self.__execute_random_walk(contender, 1)
            # contender.add_proxy(p)  # should this be done at all?? what is it's meaning?

    def __execute_random_walk(self, node: NodeModel, length: int):
        """
        Execute a random walk on the network from the given node in the given network

        :param node:
        :return: proxy
        """
        if length > 0:
            # get the neighbors
            neighbors = self.__network.get_nodes_neighbors(node)
            # select randomly the next node
            next_node = neighbors[random.randint(0, len(neighbors) - 1)]
            # continue further with the walk
            return self.__execute_random_walk(next_node, length - 1)
        else:
            return node
        pass

    pass
