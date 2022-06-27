import metronetwork as mn
import networkx as nx
import os

class Seoul():
    def __init__(self):
        self.line_info = mn.dataloader.read_seoul_metro()
        self.stations = mn.dataloader.name_fr_mapping(self.line_info)
        self.mapping = mn.dataloader.fr_station_mapping(self.line_info)

    def graph(self):
        model_path = os.path.join(mn.utils.installpath, 'data', 'seoulgraph.gpickle')
        G = nx.read_gpickle(model_path)

    def station(self, name):
        return self.stations.get(name)

    def get_station_name(self, fr_list):
        name = []
        for fr in fr_list:
            name.append(self.line_info.get(fr)[0])
        return name

    def makeTransferNameList(self):
        transfer = {}
        for fr, name_line in self.line_info.items():
            transfer.setdefault(name_line[0], set()).add(fr)
        return [key for key, values in transfer.items() if len(values) > 1]

    def makeTransferFrList(self):
        transfer = {}
        for fr, name_line in self.line_info.items():
            transfer.setdefault(name_line[0], set()).add(fr)
        return [values for key, values in transfer.items() if len(values) > 1]

    def makeTransferStationSameFr(self):
        transfer_station = {}
        for station in self.makeTransferNameList():
            line_list = []
            for fr, name_line in self.line_info.items():
                if station == name_line[0]:
                    line_list.append(fr)
            transfer_station[station]=line_list
        return transfer_station

    def makeSeoulMetroGraph(self):
        od = self.line_info
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
                    G.add_edge(tempEdge, fr, weight=2)
                    tempEdge = 'P144'
                    continue
                # exceptional Seodongtan station
                elif fr == 'P157-1':
                    G.add_edge(tempEdge, fr, weight=2)
                    tempEdge = 'P157'
                    continue
                elif fr == '310':
                    pass
                # for connect Wonheung with Wondang, Samsong
                elif fr == '318':
                    G.add_edge(tempEdge, '309', weight=2)
                    G.add_edge('309', fr, weight=2)
                elif fr == '234-1':
                    pass
                elif fr == 'D7':
                    pass
                elif fr in circular_railway_line6[:-1]:
                    continue
                else:
                    G.add_edge(tempEdge, fr, weight=2)
            
            tempEdge = fr
            line_number = name_line[1]

        # for belt line in Line 2
        G.add_edge('243', '201', weight=2)
        # for branch line in Line 2
        G.add_edge('211', '211-1', weight=2)
        G.add_edge('234', '234-1', weight=2)
        # for departing for Sinchang Line 1
        G.add_edge('141', 'P142', weight=2)
        # for departing for Macheon Line 5
        G.add_edge('548', 'P549', weight=2)
        # for Jungang line connecting to Kyeongui Line
        G.add_edge('K110', 'K826', weight=2)
        G.add_edge('K826', 'K312', weight=2)
        # connect Gajwa with Sinchon station in Kyeongui Line
        G.add_edge('K315', 'P312', weight=2)
        # connect Gulpocheon with Bupyeong-gu office in Line 7
        G.add_edge('758', '759', weight=2)
        # connect Yangjae citizens' forest with Cheonggyesan in Shinbundang Line
        G.add_edge('D9', 'D10', weight=2)
        # for circular railway line 6
        DG = nx.MultiDiGraph()
        tempEdge = '610'
        for fr in circular_railway_line6:
            DG.add_node(fr, station='')
            DG.add_edge(tempEdge, fr, weight=2)
            tempEdge = fr

        G.add_nodes_from(DG)
        G.add_edges_from(DG.edges())
        # G = DG.to_undirected()

        # transfer_list = self.makeTransferNameList()

        transfer_station = self.makeTransferStationSameFr()
        
        for station_name, fr_list in transfer_station.items():
            fr_list_size = len(fr_list) -1
            for idx, fr_name in enumerate(fr_list):
                if idx < fr_list_size:
                    for i in range(idx, fr_list_size):
                        G.add_edge(fr_list[idx], fr_list[i+1], weight=6)
        return G


if __name__ == '__main__':
    seoul = Seoul()
    G = seoul.makeSeoulMetroGraph()
    # print(G.edges())
    print(G.neighbors('234-1'))
    print(nx.number_of_nodes(G))
    # print(nx.shortest_path(G, source="237", target="410"))
    # print(nx.dijkstra_path(G, "611", "615"))
    #print(nx.single_source_dijkstra_path(G, "410"))
    #print([p for p in nx.all_shortest_paths(G, source="410", target="220")])
    # print(nx.shortest_path(G,source="138",target="234-4"))
    # print(nx.shortest_path_length(G,source="138",target="234-4"))