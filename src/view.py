from src.network_model import NetworkModel
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import shutil


class View(object):

    def __init__(self, model: NetworkModel):
        if(os.path.exists("./graphs")):
            shutil.rmtree('./graphs')
        os.mkdir("./graphs")
        self.c = 0
        self.model = model
        self.graph = nx.Graph()
        self.pos = None
        self.make_graph(model)
        pass

    def render(self):
        contender_ids = [contender.id for contender in self.model.contenders]

        proxi_ids = []
        [proxi_ids.extend(contender.get_proxies) for contender in self.model.contenders]
        proxi_ids=[proxi.id for proxi in proxi_ids]

        winner_receiver_ids = [node.id for node in self.model.nodes if node.is_winner_received]

        leader = [node.id for node in self.model.nodes if node.is_leader]

        self.show_graph(contender_ids, proxi_ids, winner_receiver_ids, leader)
        pass

    def make_graph(self, model: NetworkModel):
        node_matrix = model.node_matrix.matrix
        rows, cols = np.where(node_matrix != 0)

        edges = zip(rows.tolist(), cols.tolist())
        self.graph.add_edges_from(edges)
        self.pos = nx.spring_layout(self.graph)

    def show_graph(self, contender_ids, proxi_ids, winner_receiver_ids, leader):
        color_map = []
        for node in self.graph:
            if node in contender_ids and node not in winner_receiver_ids:
                color_map.append('yellow')
            elif (node in proxi_ids and node not in winner_receiver_ids):
                color_map.append('blue')
            elif node in winner_receiver_ids and node not in leader:
                color_map.append('red')
            elif node in leader:
                color_map.append('green')
            else:
                color_map.append('#F4D5BB')

        plt.figure(1, figsize=(16, 11))
        nx.draw_networkx(self.graph, self.pos, node_color=color_map, node_size = 500, scale = 200, dim=3)
        plt.savefig("./graphs/"+ str(self.c) +".png", format="PNG")
        plt.cla()
        plt.clf()
        self.c = self.c+1
        #plt.show()
        pass
