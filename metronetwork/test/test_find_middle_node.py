import unittest
import networkx as nx
from metronetwork import Seoul


class FindMiddleTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindMiddleTest, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_find_middle(self):
		G = self.seoul.make_seoul_metro_network()
		route_a = nx.shortest_path(G, "911", "915")
		route_b = nx.shortest_path(G, "911", "241")
		route_c = nx.shortest_path(G, "915", "241")
		route_a_edges = nx.bfs_edges(G, source="911", depth_limit=len(route_a))
		route_b_edges = nx.bfs_edges(G, source="241", depth_limit=len(route_b))
		route_c_edges = nx.bfs_edges(G, source="915", depth_limit=len(route_c))
		candidate_list = []
		candidate_list = list(set([item for t in route_a_edges for item in t]) & set([item for t in route_b_edges for item in t]))
		candidate_list = list(set(candidate_list) & set([item for t in route_c_edges for item in t]))
		candidates = set(candidate_list)
		route_nodes = {}

		for station in candidates:
			cost_a = nx.shortest_path_length(G, "911", station)
			cost_b = nx.shortest_path_length(G, "241", station) 
			cost_c = nx.shortest_path_length(G, "915", station)
			route_nodes[station] = cost_a+cost_b+cost_c

		self.assertTrue('913', min(route_nodes.items(), key=lambda x: x[1])[0])


if __name__ == '__main__':
    unittest.main()