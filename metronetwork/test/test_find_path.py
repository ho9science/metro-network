import unittest
import networkx as nx
from metronetwork import Seoul


class FindPathTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindPathTest, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_suyu_to_dangsan(self):
		G = self.seoul.make_seoul_metro_network()
		suyu_to_dangsan = ['414', '415', '416', '417', '418', '419', '420', '421', '422', '205', '204', '203', '202', '201', '243', '242', '241', '240', '239', '238', '237']
		length, path = nx.bidirectional_dijkstra(G, "414", "237")
		self.assertTrue(path == suyu_to_dangsan)

	def test_dangsan_to_gaepo(self):
		G = self.seoul.make_seoul_metro_network()
		dangsan_to_gaepo = ['913', '914', '915', '916', '917', '918', '919', '920', '921', '922', '923', '924', '925', '926', '927', 'K214', 'K215', 'K216', 'K217', 'K218', 'K219']
		length, path = nx.bidirectional_dijkstra(G, '913', 'K219') 
		self.assertTrue(path == dangsan_to_gaepo)

	def test_youngsan_to_cityhall(self):
		G = self.seoul.make_seoul_metro_network()
		yongsan_to_cityhall = ['용산', '남영', '서울역', '시청']
		length, path = nx.bidirectional_dijkstra(G, '135', '132')
		self.assertTrue(self.seoul.get_stations_name(path)
		 == yongsan_to_cityhall)
	
	def test_eumngam_circular(self):
		G = self.seoul.make_seoul_metro_network()
		saejeol_to_gusan = ['616', '610', '611', '612', '613', '614', '615']
		length, path = nx.bidirectional_dijkstra(G, '616', '615')
		self.assertTrue(path == saejeol_to_gusan)
		gusan_to_yeokchon = ['615', '610', '611']
		length, path = nx.bidirectional_dijkstra(G, '615', '611')
		self.assertTrue(path == gusan_to_yeokchon)




if __name__ == '__main__':
    unittest.main()