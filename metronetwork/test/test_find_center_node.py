import unittest
import networkx as nx
import metronetwork as mn


class FindCenterTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindCenterTest, self).__init__(*args, **kwargs)
		self.seoul = mn.Seoul()
		self.G = self.seoul.make_seoul_metro_network()
	
	def test_find_center(self):
		# result = mn.find_center(self.G, ["419", "132", "209"])
		result = mn.find_center(self.G, ["142", "D19", "K228"])
		print(result.iloc[0]['station'])
	
	def test_find_center_top5(self):
		result = mn.find_center_top5(self.G, ["234-3", "323", "520"])
		print(result)
	
	def test_find_center_one(self):
		result = mn.find_center_one(self.G, ["751", "351", "410"])
		print(result)
	

if __name__ == '__main__':
    unittest.main()