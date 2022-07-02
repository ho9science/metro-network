import csv
import io
import collections
from itertools import combinations
import json
import os
import pandas


filename = '서울교통공사 노선별 지하철역 정보.csv'
opendata = os.path.join(os.path.abspath("metronetwork"), 'data', filename)

def read_seoul_metro():
	samdasu = {}
	df = pandas.read_csv(opendata, sep=',', encoding='CP949')
	for rows in df.values:
		li = []
		li.append(str(rows[1]))
		li.append(str(rows[3]))
		samdasu[rows[4]] = li
	od = collections.OrderedDict(sorted(samdasu.items(), key=str))
	return od

def read_seoul_subway():
	df = pandas.read_csv(opendata, sep=',', encoding='CP949')
	df = df.sort_values([df.columns[3], df.columns[4]])
	return df

def readSeoulMetro():
	samdasu = {}
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
			samdasu[obj[3]] = li

	od = collections.OrderedDict(sorted(samdasu.items()))
	return od	

def name_fr_mapping(od):
	mapping = {}
	for fr, name_line in od.items():
		mapping[name_line[0]] = fr
	return mapping

def fr_station_mapping(od):
	mapping = {}
	for fr, name_line in od.items():
		mapping[fr] = name_line[0]
	return mapping

def read_seoul_metro_transfer():
	pass

def load_edges():
	edgedata = os.path.join(os.path.abspath("metronetwork"), 'data', "edge_list.json");
	with open(edgedata, "r", encoding="UTF-8") as f:
		data = json.loads(f.read())
	return data

def load_transfers():
	transferdata = os.path.join(os.path.abspath("metronetwork"), 'data', "transfer_list.json");
	with open(transferdata, "r", encoding="UTF-8") as f:
		transfers = json.loads(f.read())
	transfer_list = []
	for key in transfers:
		transfer_list.append(list(combinations(transfers[key], 2)))
	return transfer_list

def load_stations():
	stationdata = os.path.join(os.path.abspath("metronetwork"), 'data', "station_list.json");
	with open(stationdata, "r", encoding="UTF-8") as f:
		stations = json.loads(f.read())
	return stations

def load_stations_name():
	stationdata = os.path.join(os.path.abspath("metronetwork"), 'data', "station_list.json");
	with open(stationdata, "r", encoding="UTF-8") as f:
		stations = json.loads(f.read())
	names = {}
	for fr_code in stations:
		name = stations.get(fr_code)[1]
		names[name] = fr_code
	return names