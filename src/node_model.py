import math
import constants


class NodeModel(object):
    """
    Node object, has inner function which is executed at each cycle
    """

    def __init__(self, id: int, is_contender: bool):
        # attributes:
        self.__id = id
        self.__contender = is_contender
        self.__leader = False
        self.__stopped = False
        self.__contenders = set()
        self.__proxies = set()
        self.__i1 = set()
        self.__i2 = set()
        self.__i3 = set()
        self.__i4 = set()
        self.__winner_received = False
        pass
    
    @property
    def is_stopped(self):
        return self.__stopped

    @property
    def is_contender(self):
        return self.__contender

    @property
    def is_leader(self):
        return self.__leader

    @property
    def id(self):
        return self.__id

    @property
    def get_proxies(self):
        return self.__proxies

    @property
    def get_contenders(self):
        return self.__contenders

    @property
    def i1(self):
        return self.__i1

    @property
    def i2(self):
        return self.__i2

    @property
    def i3(self):
        return self.__i3

    @property
    def i4(self):
        return self.__i4

    @property
    def is_winner_received(self):
        return self.__winner_received

    def receive_winner(self):
        if not self.is_leader:
            self.__contender = False
        self.__winner_received = True

    def stop(self):
        self.__stopped = True
        pass

    def set_i1(self, i1):
        self.__i1 = i1
        pass

    def set_i2(self, i2):
        self.__i2 = i2
        pass

    def set_i3(self, i3):
        self.__i3 = i3
        pass

    def set_i4(self, i4):
        self.__i4 = i4

    def send_winner_to_contenders(self, view):
        for contender in self.__contenders:
            if not contender.is_winner_received:
                contender.receive_winner()
                contender.send_winner_to_proxies(view)
                contender.stop()
                view.render()

    def send_winner_to_proxies(self, view):
        for proxy in self.__proxies:
            if not proxy.is_winner_received:
                proxy.receive_winner()
                proxy.send_winner_to_contenders(view)
                view.render()

    def proxy_distinctness(self, contender):
        return len([c for c in self.__contenders if c.id == contender.id]) == 1

    def contender_distinctness(self, network_size):
        limit = int((constants.c2 / 2) * math.sqrt(network_size * math.log10(network_size)))
        distinct_proxies = [proxy for proxy in self.__proxies if proxy.proxy_distinctness(self)]
        return len(distinct_proxies) >= limit

    def contender_intersection(self, network):
        limit = int((3/4) * constants.c1 * math.log10(network))
        set_of_adj_cont = set()
        for adj_cont in self.__i2:
            set_of_adj_cont.add(adj_cont)
        return len(set_of_adj_cont) >= limit

    def add_proxy(self, proxy_node):
        if self.is_contender and proxy_node.id != self.id:
            # if proxy_node not in self.__proxies:
            self.__proxies.add(proxy_node)
            pass
        pass

    def add_contender(self, contender_node):
        if not self.is_contender and contender_node.id != self.id:
            self.__contenders.add(contender_node)
            pass
        pass

    def set_id(self, id: int):
        """
        Sets the id for the node model

        :return:
        """
        self.__id = id
        pass

    def set_if_contender(self, b: bool):
        """
        Set bool as value for the contender attribute

        :param b:
        :return:
        """
        self.__contender = b
        pass

    def set_as_leader(self):
        """
        Set the node to be a leader

        :return:
        """
        self.__leader = True
        pass

    pass