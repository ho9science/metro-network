import metronetwork as mn
import networkx as nx
import statistics 
import pandas as pd


def find_middle(G, nodes):
    if len(nodes) != 3:
        print("now only 3 node possible")
        return
    candidates = search_candidates_nodes(G, nodes)
    route_nodes = {}
    for station in candidates:
        cost_a = nx.dijkstra_path_length(G, nodes[0], station)
        cost_b = nx.dijkstra_path_length(G, nodes[1], station)
        cost_c = nx.dijkstra_path_length(G, nodes[2], station)
        route_nodes[station] = cost_a+cost_b+cost_c
    return route_nodes


def find_middle_sort(G, nodes):
    middles = find_middle(G, nodes).items()
    min_weight = min(middles, key=lambda x: x[1])[1]
    return [key for key, weight in middles if weight == min_weight]


def find_middle_one(G, nodes):
    return min(find_middle(G, nodes).items(), key=lambda x: x[1])[0]


def find_center(G, nodes):
    df = pd.DataFrame()
    if len(nodes) != 3:
        print("now only 3 node possible")
        return
    candidates = search_candidates_nodes(G, nodes)
    for station in candidates:
        cost_a = nx.dijkstra_path_length(G, nodes[0], station)
        cost_b = nx.dijkstra_path_length(G, nodes[1], station)
        cost_c = nx.dijkstra_path_length(G, nodes[2], station)
        cost_avg = statistics.mean([cost_a, cost_b, cost_c])
        cost_stdev = statistics.stdev([cost_a, cost_b, cost_c])
        df2 = pd.DataFrame({"station": [station], "avg": [cost_avg], "stdev": [cost_stdev], "score":[cost_avg+cost_stdev]})
        df = pd.concat([df, df2])
    df = df[['station', 'score']].sort_values(['score'])
    return df


def find_center_top5(G, nodes):
    centers = find_center(G, nodes).head(5).set_index('station')['score'].to_dict()
    return list(centers.keys())


def find_center_one(G, nodes):
    centers = find_center(G, nodes).head(1).set_index('station')['score'].to_dict()
    return min(centers, key=lambda x: x[1])


def search_candidates_nodes(G, nodes):
    candidates = []
    route_a = nx.dijkstra_path(G, nodes[0], nodes[2])
    route_b = nx.dijkstra_path(G, nodes[0], nodes[1])
    route_c = nx.dijkstra_path(G, nodes[1], nodes[2])
    route_a_edges = nx.bfs_edges(G, source=nodes[0], depth_limit=len(route_a))
    route_b_edges = nx.bfs_edges(G, source=nodes[1], depth_limit=len(route_b))
    route_c_edges = nx.bfs_edges(G, source=nodes[2], depth_limit=len(route_c))
    candidates = list(set([item for t in route_a_edges for item in t]) & set([item for t in route_b_edges for item in t]))
    candidates = list(set(candidates) & set([item for t in route_c_edges for item in t]))
    return candidates