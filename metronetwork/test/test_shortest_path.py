import unittest
import networkx as nx
from metronetwork import Seoul


class FindShortestPathTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindShortestPathTest, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_shortest_path(self):
		G = self.seoul.makeSeoulMetroGraph()
		suyu_to_dangsan = ['414', '415', '416', '417', '418', '419', '420', '421', '422', '205', '204', '203', '202', '201', '243', '242', '241', '240', '239', '238', '237']
		print(nx.shortest_path(G, "414", "237"))
		self.assertFalse(nx.shortest_path(G, "414", "237")== suyu_to_dangsan)

	def test_dijkstra_name(self):
		G = self.seoul.makeSeoulMetroGraph()
		dangsan_to_gaepo = ['913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', 'K214', 'K215', 'K216', 'K217', 'K218', 'K219']
		self.assertFalse(self.seoul.get_station_name(nx.shortest_path(G, '913', 'K219')) 
			== self.seoul.get_station_name(dangsan_to_gaepo))


if __name__ == '__main__':
    unittest.main()