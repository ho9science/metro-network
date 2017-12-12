import csv
import io
import collections

import matplotlib.pyplot as plt
import networkx as nx

samdasu = {}
with io.open('seoulmetro.csv', mode='r', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    next(spamreader)
    for row in spamreader:
        str = "\" ".join(row)
        str = str.replace('\"','')
        obj = str.rstrip().split(',')
        
        li = []
        li.append(obj[1])
        li.append(obj[2])
        samdasu[obj[3]] = li

G = nx.Graph()        
od = collections.OrderedDict(sorted(samdasu.items()))

tempEdge = ""
tempBranch = ""
for fr,values in od.items():
    G.add_node(fr,station=values[0])
    
    if not tempEdge :        
        pass
    else:
        if fr[0] == tempEdge[0] and len(fr) >= len(tempEdge):
            G.add_edge(tempEdge,fr,weight=2)
        else:
            G.add_edge(tempBranch,fr,weight=2)
        
        if len(fr)>len(tempEdge):
            tempBranch = tempEdge
        
    tempEdge = fr
transfer = {}
temp_name = ""
for k, v in od.items():
    
    if not temp_name :        
        pass
    else:
        for k2, v2 in od.items():
            transfer.setdefault(v2[0], set()).add(k2)
           
    temp_name=v[0]
    
transfer_list = [key for key, values in transfer.items() if len(values) > 1]
transfer_fr_list = [values for key, values in transfer.items() if len(values) > 1]

print(transfer_fr_list)
transfer_station = {}


for station in transfer_list:
    line_list = []
    for k, v in od.items():
        if station == v[0]:
            line_list.append(k)
    transfer_station[station]=line_list

for key, value in transfer_station.items():
    temp_value = ""
    for i in value:
        if not temp_value :        
            pass
        else:
            G.add_edge(temp_value,i,weight=4)
        temp_value = i

# print(nx.shortest_path(G,source="138",target="234-4"))
# print(nx.shortest_path_length(G,source="138",target="234-4"))
