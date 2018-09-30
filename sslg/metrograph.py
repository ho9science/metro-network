import csv
import io
import collections
import os

import matplotlib.pyplot as plt
import networkx as nx


def readSeoulMetro():
    samdasu = {}
    opendata = os.path.join(os.path.abspath("sslg"), 'data', 'seoulmetro.csv')
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

def makeTransferNameList(od):
    transfer = {}
    for fr, name_line in od.items():
        transfer.setdefault(name_line[0], set()).add(fr)
    return [key for key, values in transfer.items() if len(values) > 1]

def makeTransferFrList(od):
    transfer = {}
    for fr, name_line in od.items():
        transfer.setdefault(name_line[0], set()).add(fr)
    return [values for key, values in transfer.items() if len(values) > 1]

def makeTransferStationSameFr(transfer_list, od):
    transfer_station = {}
    for station in transfer_list:
        line_list = []
        for fr, name_line in od.items():
            if station == name_line[0]:
                line_list.append(fr)
        transfer_station[station]=line_list
    
    return transfer_station

def makeSeoulMetroGraph():
    od = readSeoulMetro()
    G = nx.Graph()
    tempEdge = '100'
    line_number = '1'
    circular_railway_line6 = ['611', '612', '613', '614', '615', '610']
    for fr, name_line in od.items():
        if fr in circular_railway_line6[:-1]:
            continue
        else: 
            G.add_node(fr, station=name_line[0])
        if name_line[1] == line_number:
            # Gyeongchun line exceptional Gwangwun Univ
            if fr == 'P119':
                continue
            # exceptional Gwangmyeon station
            elif fr == 'P144-1':
                G.add_edge(tempEdge, fr, weight=0.9)
                tempEdge = 'P144'
                continue
            # exceptional Seodongtan station
            elif fr == 'P157-1':
                G.add_edge(tempEdge, fr, weight=0.9)
                tempEdge = 'P157'
                continue
            elif fr == '310':
                continue
            # for connect Wonheung with Wondang, Samsong
            elif fr == '318':
                G.add_edge(tempEdge, '309', weight=0.9)
                G.add_edge('309', fr, weight=0.9)
            elif fr == '234-1':
                continue
            elif fr == 'D7':
                continue
            elif fr in circular_railway_line6[:-1]:
                continue
            else:
                G.add_edge(tempEdge, fr, weight=0.9)
        
        tempEdge = fr
        line_number = name_line[1]
    # for belt line in Line 2
    G.add_edge('243', '201', weight=0.9)
    # for branch line in Line 2
    G.add_edge('211', '211-1', weight=0.9)
    G.add_edge('234', '234-1', weight=0.9)
    # for departing for Sinchang Line 1
    G.add_edge('141', 'P142', weight=0.9)
    # for departing for Macheon Line 5
    G.add_edge('548', 'P549', weight=0.9)
    # for Jungang line connecting to Kyeongui Line
    G.add_edge('K110', 'K826', weight=0.9)
    G.add_edge('K826', 'K312', weight=0.9)
    # connect Gajwa with Sinchon station in Kyeongui Line
    G.add_edge('K315', 'P312', weight=0.9)
    # connect Gulpocheon with Bupyeong-gu office in Line 7
    G.add_edge('758', '759', weight=0.9)
    # connect Yangjae citizens' forest with Cheonggyesan in Shinbundang Line
    G.add_edge('D9', 'D10', weight=0.9)
    # for circular railway line 6
    DG = nx.MultiDiGraph()
    tempEdge = '610'
    for fr in circular_railway_line6:
        DG.add_node(fr, station='')
        DG.add_edge(tempEdge, fr, weight=0.9)
        tempEdge = fr

    G.add_nodes_from(DG)
    G.add_edges_from(DG.edges())

    transfer_list = makeTransferNameList(od)

    transfer_station = makeTransferStationSameFr(transfer_list, od)
    
    for station_name, fr_list in transfer_station.items():
        fr_list_size = len(fr_list) -1
        for idx, fr_name in enumerate(fr_list):
            if idx < fr_list_size:
                for i in range(idx, fr_list_size):
                    G.add_edge(fr_list[idx], fr_list[i+1], weight=100)
    return G

if __name__ == '__main__':
    G = makeSeoulMetroGraph()
    # print(G.edges())
    # print(G.neighbors('610'))
    # print(nx.shortest_path(G, source="237", target="410"))
    print(nx.dijkstra_path(G, "410", "237"))
    #print(nx.single_source_dijkstra_path(G, "410"))
    #print([p for p in nx.all_shortest_paths(G, source="410", target="220")])
    # print(nx.shortest_path(G,source="138",target="234-4"))
    # print(nx.shortest_path_length(G,source="138",target="234-4"))
