import os
import unittest
import networkx as nx
from metronetwork import Seoul
from metronetwork import metro_utils
import time


class GraphTest(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(GraphTest, self).__init__(*args, **kwargs)

	def test_write_gpickle(self):
		self.start_time = time.time()
		self.seoul = Seoul()
		G = self.seoul.make_seoul_metro_network()
		model_path = os.path.join(metro_utils.INSTALLED_PATH, 'data', 'seoulgraph.gpickle')
		nx.write_gpickle(G, model_path)
		print("--- complete create model ---")

	def test_read_gpickle(self):
		start_time = time.time()
		model_path = os.path.join(metro_utils.INSTALLED_PATH, 'data', 'seoulgraph.gpickle')
		G = nx.read_gpickle(model_path)
		self.assertTrue(767==nx.number_of_nodes(G))