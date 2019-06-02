import unittest
import networkx as nx
from subwaylinegraph import Seoul as slg
import json
    
class FloyWarshall(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FloyWarshall, self).__init__(*args, **kwargs)
		self.seoul = slg.Seoul()

	def test_floyd(self):
		G = self.seoul.makeSeoulMetroGraph()		
		with open('floyd.txt', 'w') as f:
			f.write(json.dumps(nx.floyd_warshall(G, weight='weight')))
		
if __name__ == '__main__':
    unittest.main()