from itertools import combinations
import metronetwork as mn
import networkx as nx
import os

LINE1_EDGE = "#0052A4"
LINE2_EDGE = "#00A84D"
LINE3_EDGE = "#EF7C1C"
LINE4_EDGE = "#00A4E3"
LINE5_EDGE = "#996CAC"
LINE6_EDGE = "#CD7C2F"
LINE7_EDGE = "#747F00"
LINE8_EDGE = "#E6186C"
LINE9_EDGE = "#BDB092"
AREX_EDGE = "#0090D2"
GYEONGUI_EDGE = "#77C4A3"
GYEONGCHUN_EDGE = "#005666"
SUINBUNDANG_EDGE = "#FABE00"
SHINBUNDANG_EDGE = "#D31145"
GYEONGGANG_EDGE = "#0054A6"
SEOHAE_EDGE = "#8FC31F"
INCHEONLINE1_EDGE = "#759CCE"
INCHEONLINE2_EDGE = "#F5A251"
EVERLINE_EDGE = "#56AD2D"
EUIJEONGBU_EDGE = "#FD8100"
UISINSEOL_EDGE = "#B7C450"
KIMPO_EDGE = "#AD8605"
SINRIM_EDGE = "#6789CA"


class Seoul():
    def __init__(self):
        self.line_edges = mn.dataloader.load_edges()
        self.line_transfer = mn.dataloader.load_transfers()
        self.stations = mn.dataloader.load_stations()
        self.stations_name = mn.dataloader.load_stations_name()

    def graph(self):
        model_path = os.path.join(mn.utils.installpath, 'data', 'seoulgraph.gpickle')
        G = nx.read_gpickle(model_path)

    def code(self, fr):
        return self.stations.get(fr)[0]
        
    def station(self, name): 
        return self.stations_name.get(name)
        
    def get_station(self, fr):
        return self.stations.get(fr)[1]

    def get_stations_name(self, fr_list):
        name = []
        for fr in fr_list:
            if self.stations.get(fr):
                name.append(self.stations.get(fr)[1])
            else:
                name.append(None)
        return name

    def station_eng(self, fr):
        return self.stations.get(fr)[2]

    def line(self, fr):
        return self.stations.get(fr)[3]

    def make_seoul_metro_network(self):
        stations = self.stations
        edges = self.line_edges
        G = nx.DiGraph()

        G.add_nodes_from(stations.keys())
        for key in edges:
            G.add_edges_from(edges.get(key), weight=2)
        transfers = self.line_transfer
        for transfer_edge in transfers:
            if lambda x: True if "A" in x else False:
                G.add_edges_from(transfer_edge, weight=10)
            else:
                G.add_edges_from(transfer_edge, weight=5)
        return G
        


if __name__ == '__main__': 
    seoul = Seoul()
    G = seoul.make_seoul_metro_network()
    print(G)
