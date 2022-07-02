import unittest
import networkx as nx
from metronetwork import Seoul


class FindPathTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindPathTest, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_dijkstra(self):
		G = self.seoul.make_seoul_metro_network()
		suyu_to_dangsan = ['414', '415', '416', '417', '418', '419', '420', '421', '422', '205', '204', '203', '202', '201', '243', '242', '241', '240', '239', '238', '237']
		self.assertTrue(nx.dijkstra_path(G, "414", "237")== suyu_to_dangsan)

	def test_dijkstra_name(self):
		G = self.seoul.make_seoul_metro_network()
		dangsan_to_gaepo = ['913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', 'K214', 'K215', 'K216', 'K217', 'K218', 'K219']
		self.assertTrue(nx.dijkstra_path(G, '913', 'K219') == dangsan_to_gaepo)

	def test_dijkstra_name(self):
		G = self.seoul.make_seoul_metro_network()
		yongsan_to_cityhall = ['용산', '남영', '서울역', '시청']
		self.assertTrue(self.seoul.get_stations_name(nx.dijkstra_path(G, '135', '132'))
		 == yongsan_to_cityhall)


if __name__ == '__main__':
    unittest.main()