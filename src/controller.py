import random
import math
from src.node_model import NodeModel
from src.network_builder import NetworkBuilder
import constants


class Controller(object):

    def __init__(self, network_size: int = 10):
        self.__pref_network_size = network_size
        self.__network = NetworkBuilder().build_network()
        self.__parallel_rw_count = int(constants.c2 * math.sqrt(self.__network.size * math.log10(self.__network.size)))
        pass

    def run(self):
        # TODO
        pass

    def __run_parallel_walks(self):
        """
        Algorithm 2 Step 1 & 2

        :return:
        """
        for contender in self.__network.contenders:
            self.__set_contender_proxies(contender)
            pass
        pass

    def __round_1(self):
        """
        Algorithm 2 Step 3.1

        :return:
        """
        for contender in self.__network.contenders:
            for proxy in contender.get_proxies:
                proxy_id = proxy.id  # TODO ??
                proxy_d = proxy.proxy_distinctness(contender)  # TODO ??
                proxy_i1 = proxy.get_contenders
                contender.set_i2 = contender.i2 + proxy_i1
                pass
            pass
        pass

    def __round_2(self):
        """
        Algorithm 2 Step 3.2

        :return:
        """
        for contender in self.__network.contenders:
            for proxy in contender.get_proxies:
                proxy.set_i3 = proxy.i3 + contender.i2
                pass
            pass
        pass

    def __round_3(self):
        """
        Algorithm 2 Step 3.3

        :return:
        """
        for contender in self.__network.contenders:
            for proxy in contender.get_proxies:
                contender.set_i4 = contender.i4 + proxy.i3
        pass

    def __stop_if_intersection_and_distinctness_are_met(self):
        """
        Algorithm 2 Step 4

        :return:
        """
        for contender in self.__network.contenders:
            if contender.contender_distinctness(self.__network.size) and \
                    contender.contender_intersection(len(self.__network.contenders)):
                contender.stop()
                pass
            pass
        # this will set the
        for contender in self.__network.contenders:
            if contender.is_stopped:
                list_of_higher_id_contenders_in_i4 = [cont for cont in contender.i4 if cont.id > contender.id]
                if not list_of_higher_id_contenders_in_i4:
                    # declare itself as leader
                    contender.set_as_leader()
                    self.__propagate_winner_messages(contender)
                pass
            pass
        pass

    def __propagate_winner_messages(self, contender: NodeModel):
        """
        Propagate the winner messages
        Algorithm 5, 6, 7

        :param contender:
        :return:
        """
        contender.send_winner_to_proxies()
        pass

    def __set_contender_proxies(self, node: NodeModel):
        """
        Runs c2*sqrt(n*log10(n)) parallel random walks to get the proxies of the Node

        :param node: NodeModel
        :return:
        """
        for _ in range(0, self.__parallel_rw_count):
            proxy = self.__execute_random_walk(node, self.__parallel_rw_count)
            proxy.add_contender(node)
            node.add_proxy(proxy)
            pass
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
