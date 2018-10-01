import unittest
import inspect
import networkx as nx
from sslg.metrograph import makeSeoulMetroGraph

    
class SslgTest(unittest.TestCase):
    def test_station(self):
        self.logPoint()
        G = makeSeoulMetroGraph()
        assert(nx.number_of_nodes(G)==695)
    
    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        print ('in %s - %s()' % (currentTest, callingFunction))
    
if __name__ == '__main__':
    unittest.main()