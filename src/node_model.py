class NodeModel(object):
    """
    Node object, has inner function which is executed at each cycle
    """

    def __init__(self, id: int, is_contender: bool):
        # attributes:
        self.__id = id
        self.__contender = is_contender
        self.__leader = False
        self.__contenders = list()
        self.__proxies = list()
        self.__i1 = list()
        self.__i2 = list()
        self.__i3 = list()
        self.__i4 = list()

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

    def proxy_distinctness(self, contender):
        return [c for c in self.__contenders if c.id == contender.id] == 1

    def add_proxy(self, proxy_node):
        if self.is_contender and proxy_node.id != self.id:
            # if proxy_node not in self.__proxies:
            self.__proxies.append(proxy_node)
            pass
        pass

    def add_contender(self, contender_node):
        if not self.is_contender and not contender_node.id != self.id:
            self.__contenders.append(contender_node)
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