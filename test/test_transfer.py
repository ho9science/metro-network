import unittest
import networkx as nx
from subwaylinegraph import Seoul as slg

    
class TransferTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LineTest, self).__init__(*args, **kwargs)
        seoul = slg.Seoul()
        self.G = seoul.makeSeoulMetroGraph()

    def test_line_3(self):
        self.assertTrue(sorted(self.G.neighbors('309'))==['317','318'])
    
if __name__ == '__main__':
    unittest.main()