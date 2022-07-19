import unittest
import networkx as nx
import metronetwork as mn


class FindMiddleTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(FindMiddleTest, self).__init__(*args, **kwargs)
		self.seoul = mn.Seoul()
		self.G = self.seoul.make_seoul_metro_network()

	def test_find_middle(self):
		result = mn.find_middle_one(self.G, ["911", "915", "241"])
		self.assertTrue('913' == result)
	
	def test_find_middle2(self):
		result = mn.find_middle_one(self.G, ["100", "K420", "I201"])
		self.assertTrue('K114' == result)
	
	# def test_find_middle3(self):
	# 	result = mn.find_middle_one(self.G, ["690", "P140", "P177"])
	# 	print(result)
	# 	self.assertTrue('K111' == result)
	
	def test_find_middle4(self):
		result = mn.find_middle_sort(self.G, ["352", "751", "410"])
		self.assertTrue(len(['K116', 'K210']) == len(result))

	def test_find_middle5(self):
		result = mn.find_middle_one(self.G, ["415", "543", "241"])
		self.assertTrue('205' == result)

	def test_find_middle_list(self):
		result = mn.find_middle_one(self.G, ["240", "212", "419"])
		self.assertTrue('205' == result)


if __name__ == '__main__':
    unittest.main()