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

    def __execute_random_walk(self, node: NodeModel, length: int):
        """
        Execute a random walk on the network from the given node in the given network

        :param node:
        :param length:
        :return:
        """
        # TODO
        pass

    pass
