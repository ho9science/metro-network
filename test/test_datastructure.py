import json
import os
import unittest
from subwaylinegraph import dataloader

    
class DatastructureTest(unittest.TestCase):

	def test_create_json(self):
		jsondata = os.path.join(os.path.abspath("subwaylinegraph"), 'data', "seoul_subway_json");
		dataloader.create_json()
		with open(jsondata, "r", encoding="UTF-8") as f:
			data = json.loads(f.read())
		self.assertTrue(767==len(data))


if __name__ == '__main__':
    unittest.main()