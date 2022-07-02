import unittest
import inspect
import networkx as nx
from metronetwork import Seoul


class SslgTest(unittest.TestCase):
    def test_station(self):
        self.logPoint()
        seoul = Seoul()
        G = seoul.make_seoul_metro_network()
        assert(nx.number_of_nodes(G)==767)

    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        print ('in %s - %s()' % (currentTest, callingFunction))
    
if __name__ == '__main__':
    unittest.main()