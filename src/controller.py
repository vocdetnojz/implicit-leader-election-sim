import random
import math
from src.node_model import NodeModel
from src.network_builder import NetworkBuilder
import constants
from src.view import View


class Controller(object):

    def __init__(self, network_size: int = 10):
        self.__pref_network_size = network_size
        self.__network = NetworkBuilder().build_network()
        print("Graph representation build done...\n")
        while len(self.__network.contenders) < 3:
            self.__network = NetworkBuilder().build_network()
        self.__parallel_rw_count = int(constants.c2 * math.sqrt(self.__network.size * math.log10(self.__network.size)))
        self.__random_walk_length = constants.tu
        # stats
        print("Contenders: ", len(self.__network.contenders))
        print("Parallel random walk count per contender: ", self.__parallel_rw_count)
        print("Parallel random walk length: ", self.__random_walk_length)
        self.__rounds = 0
        self.view = View(self.__network)
        self.view.render()
        pass

    @property
    def net(self):
        return self.__network

    def run(self):
        # algorithm 1 is basically implemented in the __init__
        self.run_algorithm_2()
        pass

    def run_algorithm_2(self):
        print("\n==================================================")
        print("Contenders's IDs before election: ", [c.id for c in self.__network.contenders])
        while self.__network.contenders and [c for c in self.__network.contenders if not c.is_stopped]:
            self.__rounds += 1
            print("--------------------------------------------------")
            print("ROUND ", self.__rounds)
            self.__run_algorithm_2_round()
            self.__random_walk_length *= 2
            print("Contenders' IDs after round: ", [c.id for c in self.__network.contenders])
            pass
        print("==================================================\n")
        print("LEADER(s): ", [c.id for c in self.__network.contenders if c.is_leader])
        print("rounds until leader selected: ", self.__rounds)
        pass

    def __run_algorithm_2_round(self):
        # step 1 2
        self.__run_parallel_walks()
        # step 3.1
        self.__round_1()
        # step 3.2
        self.__round_2()
        # step 3.3
        self.__round_3()
        # step 4, 5, 6, 7
        self.__stop_if_intersection_and_distinctness_are_met()
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
                # proxy_id = proxy.id  # skipped for the simulation
                # proxy_d = proxy.proxy_distinctness(contender)  # distinctness will be determined later on
                proxy_i1 = proxy.get_contenders
                contender.set_i2(set.union(contender.i2, proxy_i1))
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
                proxy.set_i3(set.union(proxy.i3, contender.i2))
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
                contender.set_i4(set.union(contender.i4, proxy.i3))
        pass

    def __stop_if_intersection_and_distinctness_are_met(self):
        """
        Algorithm 2 Step 4, 5, 6, 7

        :return:
        """
        for contender in self.__network.contenders:
            if contender.contender_distinctness(self.__network.size) and contender.contender_intersection(len(self.__network.contenders)):
                contender.stop()
                pass
            pass
        # this will determine the leader and propagate the winner messages
        for contender in self.__network.contenders:
            if contender.is_stopped:
                list_of_higher_id_contenders_in_i4 = [cont for cont in contender.i4 if cont.id > contender.id]
                if not list_of_higher_id_contenders_in_i4:
                    # declare itself as leader
                    contender.set_as_leader()
                    self.__propagate_winner_messages(contender)
                pass
            pass
        for contender in self.__network.contenders:
            if contender.is_stopped and not contender.is_leader:
                # node is not a contender anymore if it stopped and it isn't the leader
                contender.set_if_contender(False)
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
        contender.send_winner_to_proxies(self.view)
        pass

    def __set_contender_proxies(self, node: NodeModel):
        """
        Runs c2*sqrt(n*log10(n)) parallel random walks to get the proxies of the Node

        :param node: NodeModel
        :return:
        """
        for _ in range(0, self.__parallel_rw_count):
            c = len(self.__network.proxies_ids)
            proxy = self.__execute_random_walk(node, self.__random_walk_length)
            proxy.add_contender(node)
            node.add_proxy(proxy)
            if len(self.__network.proxies_ids) > c:
                self.view.render()
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
