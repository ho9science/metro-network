import unittest
import inspect
import networkx as nx
from subwaylinegraph import Seoul as slg

    
class SslgTest(unittest.TestCase):
    def test_station(self):
        self.logPoint()
        seoul = slg.Seoul()
        G = seoul.makeSeoulMetroGraph()
        print(nx.number_of_nodes(G))
        assert(nx.number_of_nodes(G)==715)
    
    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        print ('in %s - %s()' % (currentTest, callingFunction))
    
if __name__ == '__main__':
    unittest.main()