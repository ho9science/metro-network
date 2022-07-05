import unittest
from metronetwork import Seoul

    
class TransferTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TransferTest, self).__init__(*args, **kwargs)
		self.seoul = Seoul()

	def test_line_3(self):
		G = self.seoul.make_seoul_metro_network()
		self.assertTrue(sorted(G.neighbors('309'))==['310'])

	def test_line_4(self):
		G = self.seoul.make_seoul_metro_network()
		self.assertTrue(sorted(G.neighbors(self.seoul.station('당고개')))==['408', '410'])
	
	def test_line_5(self):
		G = self.seoul.make_seoul_metro_network()
		self.assertTrue(sorted(G.neighbors(self.seoul.station('까치산')))==['234-4', '517', '519'])

	def test_line_6(self):
		G = self.seoul.make_seoul_metro_network()
		self.assertTrue(self.seoul.get_stations_name(G.neighbors('647'))==['화랑대', '신내'])



if __name__ == '__main__':
    unittest.main()