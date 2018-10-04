import csv
import io
import collections
import os


def readSeoulMetro():
	samdasu = {}
	opendata = os.path.join(os.path.abspath("subwaylinegraph"), 'data', '서울시_노선별_지하철역_정보.csv')
	with io.open(opendata, mode='r', encoding='utf-8') as csvfile:
		datareader = csv.reader(csvfile, delimiter=' ', quotechar=',')
		next(datareader)
		for row in datareader:
			str = "\" ".join(row)
			str = str.replace('\"','')
			obj = str.rstrip().split(',')

			li = []
			li.append(obj[1])
			li.append(obj[2])
			samdasu[obj[3].capitalize()] = li

	od = collections.OrderedDict(sorted(samdasu.items()))
	return od
