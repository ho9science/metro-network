import unittest
import networkx as nx
import collections
from subwaylinegraph import dataloader

class DataLoaderTest(unittest.TestCase):

	def test_read_csv(self):
		data = dataloader.read_seoul_metro()
		self.assertTrue(767==len(data))

	def test_read_transfer_csv(self):
		data = dataloader.read_seoul_metro_transfer()
		
if __name__ == '__main__':
    unittest.main()