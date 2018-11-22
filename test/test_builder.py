import unittest
from src.network_builder import NetworkBuilder


class TestBuilder(unittest.TestCase):

    def test_builder(self):
        nb = NetworkBuilder()
        net = nb.build_network()

        # net.nodes[45]
        pass

    pass
