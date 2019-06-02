import json
from pprint import pprint
import pandas as pd

with open('floyd.json', 'r') as f:
	data = json.load(f)
	df = pd.DataFrame(data)
	pprint(df)


