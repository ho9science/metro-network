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
    tempEdge = ""
    tempBranch = ""
    for fr,values in od.items():
        G.add_node(fr,station=values[0])

        if not tempEdge :        
            pass
        else:
            if fr[0] == tempEdge[0]:
                if len(fr) >= len(tempEdge):
                    if fr == 'K210' or fr == 'P119':
                        continue
                    else:
                        G.add_edge(tempEdge, fr, weight=0.9)
                else:
                    G.add_edge(tempBranch, fr, weight=2.1)
                

            if len(fr) > len(tempEdge):
                tempBranch = tempEdge

        tempEdge = fr
    # for belt line line 2
    G.add_edge('243', '201', weight=0.9)
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
    print(nx.shortest_path(G,source="410",target="720"))
    # print(nx.dijkstra_path(G,"237","410"))
    #print(nx.single_source_dijkstra_path(G, "410"))
    #print([p for p in nx.all_shortest_paths(G, source="410", target="220")])
    # print(nx.shortest_path(G,source="138",target="234-4"))
    # print(nx.shortest_path_length(G,source="138",target="234-4"))
