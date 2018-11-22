class NodeModel(object):
    """
    Node object, has inner function which is executed at each cycle
    """

    def __init__(self, id: int, is_contender: bool):
        # attributes:
        self.__id = id
        self.__contender = is_contender
        self.__leader = False
        self.__proxies = []
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

    def add_proxy(self, proxy_node):
        if proxy_node not in self.__proxies:
            self.__proxies.append(proxy_node)

    def set_id(self, id: int):
        """
        Sets the id for the node model

        :return:
        """
        self.__id = id

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