import unittest
from metronetwork import Seoul


class LineTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LineTest, self).__init__(*args, **kwargs)
        seoul = Seoul()
        self.stations = seoul.stations

    def test_station_1(self):
        self.assertTrue(['1916', '소요산', 'Soyosan', '01호선']==self.stations.get('100'))
    
if __name__ == '__main__':
    unittest.main()