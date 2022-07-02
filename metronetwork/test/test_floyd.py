import unittest
import networkx as nx
from metronetwork import Seoul
import json


class FloyWarshall(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FloyWarshall, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_floyd(self):
		G = self.seoul.make_seoul_metro_network()		
		with open('floyd.txt', 'w') as f:
			f.write(json.dumps(nx.floyd_warshall(G, weight='weight')))
		
if __name__ == '__main__':
    unittest.main()