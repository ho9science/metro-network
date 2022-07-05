import metronetwork.metro_utils as utils
from itertools import permutations
import json
import pandas


def read_seoul_metro():
	filename = '서울교통공사 노선별 지하철역 정보.csv'
	df = pandas.read_csv(utils.data_path(filename), sep=',', encoding='CP949')
	df = df.sort_values([df.columns[3], df.columns[4]])
	return df

def load_edges():
	edgedata = utils.data_path("edge_list.json");
	with open(edgedata, "r", encoding="UTF-8") as f:
		data = json.loads(f.read())
	return data

def load_transfers():
	transferdata = utils.data_path("transfer_list.json");
	with open(transferdata, "r", encoding="UTF-8") as f:
		transfers = json.loads(f.read())
	transfer_list = []
	for key in transfers:
		transfer_list.append(list(permutations(transfers[key], 2)))
	return transfer_list

def load_stations():
	stationdata = utils.data_path("station_list.json");
	with open(stationdata, "r", encoding="UTF-8") as f:
		stations = json.loads(f.read())
	return stations

def load_stations_name():
	stationdata = utils.data_path("station_list.json");
	with open(stationdata, "r", encoding="UTF-8") as f:
		stations = json.loads(f.read())
	names = {}
	for fr_code in stations:
		name = stations.get(fr_code)[1]
		names[name] = fr_code
	return names