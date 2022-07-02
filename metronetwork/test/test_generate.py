import unittest
from metronetwork import dataloader
from metronetwork import generate


class GenerateTest(unittest.TestCase):
    def test_generate_edges(self):
        generate.generate_edge()
        data = dataloader.load_edges()
        self.assertTrue(22==len(data))
    
if __name__ == '__main__':
    unittest.main()