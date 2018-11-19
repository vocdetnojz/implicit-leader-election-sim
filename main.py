import math
import random


class NodeModel(object):
    """
    Node object, has inner function which is executed at each cycle
    """

    def __init__(self, id, is_contender):
        # TODO
        # state attributes:
        self.__id = id
        self.__contender = is_contender
        self.__leader = False
        pass

    @property
    def is_contender(self):
        return self.__contender

    @property
    def is_leader(self):
        return self.__leader

    @property
    def id(self):
        return self.__id

    def set_if_contender(self, b: bool):
        """
        Set bool as value for the contender attribute

        :param b:
        :return:
        """
        self.__contender = b

    def set_as_leader(self):
        """
        Set the node to be a leader

        :return:
        """
        self.__leader = True
        pass

    pass


class NetworkModel(object):
    """
    Network Model which contains the Nodes and the edges in between

    """

    def __init__(self):
        self.__nodes = list()
        self.__edges = None  # TODO, csucsmatrix?

    @property
    def size(self):
        return len(self.__nodes)

    pass


class View(object):

    def __init__(self):
        pass

    def render(self, model: NetworkModel):
        pass

    pass


class Controller(object):

    def __init__(self):
        self.__network = None  # TODO
        pass

    def run(self):
        # TODO
        pass

    def __generate_network_model(self, n: int):
        """
        Create a 4-regular super-node graph model based on size N

        :param n:
        :return:
        """
        return NetworkModel()

    def __execute_random_walk(self, node: NodeModel, length: int):
        """
        Execute a random walk on the network from the given node in the given network

        :param node:
        :param length:
        :return:
        """
        # TODO
        pass

    def __generate_node_id(self):
        """
        Generate a node id

        :return:
        """
        # TODO

    def __set_if_contends(self, node: NodeModel, c1 = 1):
        """
        Calculate a boolean value for a node which will set if it's a contender

        :param c1: tuner constant
        :return:
        """
        node.set_if_contender(random.random() <= c1 * math.log10(self.__network.size) / self.__network.size)
        return node.is_contender

    pass


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.run()
    pass
