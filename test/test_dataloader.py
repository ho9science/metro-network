import unittest
import networkx as nx
import collections
from subwaylinegraph import dataloader

class DataLoaderTest(unittest.TestCase):

	def test_read_csv(self):
		data = dataloader.read_seoul_metro()
		self.assertTrue(715==len(data))

if __name__ == '__main__':
    unittest.main()