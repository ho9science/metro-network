import unittest
import networkx as nx
import collections
from subwaylinegraph import Seoul as slg

    
class LineTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LineTest, self).__init__(*args, **kwargs)
        seoul = slg.Seoul()
        self.line_info = seoul.line_info

    def test_station_1(self):
        self.assertTrue(['소요산', '01호선']==self.line_info.get('100'))
    
if __name__ == '__main__':
    unittest.main()