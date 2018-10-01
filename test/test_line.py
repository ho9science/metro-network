import unittest
import networkx as nx
from sslg.metrograph import makeSeoulMetroGraph

    
class LineTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LineTest, self).__init__(*args, **kwargs)
        self.G = makeSeoulMetroGraph()

    def test_line_3(self):
        print(self.G.neighbors('309'))
        self.assertTrue(sorted(self.G.neighbors('309'))==['317','318'])
    
if __name__ == '__main__':
    unittest.main()