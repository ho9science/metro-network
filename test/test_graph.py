import os
import unittest
import networkx as nx
from subwaylinegraph import Seoul as slg
from subwaylinegraph import utils
import time
class GraphTest(unittest.TestCase):


	def __init__(self, *args, **kwargs):
		super(GraphTest, self).__init__(*args, **kwargs)

	def test_write_gpickle(self):
		self.start_time = time.time()
		self.seoul = slg.Seoul()
		G = self.seoul.makeSeoulMetroGraph()
		model_path = os.path.join(utils.installpath, 'data', 'seoulgraph.gpickle')
		nx.write_gpickle(G, model_path)
		print("--- complete create model ---")

	def test_read_gpickle(self):
		start_time = time.time()
		model_path = os.path.join(utils.installpath, 'data', 'seoulgraph.gpickle')
		G = nx.read_gpickle(model_path)
		self.assertTrue(767==nx.number_of_nodes(G))