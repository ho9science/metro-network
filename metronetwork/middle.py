import metronetwork as mn
import networkx as nx


def find_middle(G, nodes):
    if len(nodes) != 3:
        print("now only 3 node possible")
        return
    route_a = nx.shortest_path(G, nodes[0], nodes[2])
    route_b = nx.shortest_path(G, nodes[0], nodes[1])
    route_c = nx.shortest_path(G, nodes[1], nodes[2])
    route_a_edges = nx.bfs_edges(G, source=nodes[0], depth_limit=len(route_a))
    route_b_edges = nx.bfs_edges(G, source=nodes[1], depth_limit=len(route_b))
    route_c_edges = nx.bfs_edges(G, source=nodes[2], depth_limit=len(route_c) )
    candidates = []
    candidates = list(set([item for t in route_a_edges for item in t]) & set([item for t in route_b_edges for item in t]))
    candidates = list(set(candidates) & set([item for t in route_c_edges for item in t]))
    route_nodes = {}

    for station in candidates:
        cost_a = nx.shortest_path_length(G, nodes[0], station)
        cost_b = nx.shortest_path_length(G, nodes[1], station)
        cost_c = nx.shortest_path_length(G, nodes[2], station)
        route_nodes[station] = cost_a+cost_b+cost_c
    return route_nodes


def find_middle_sort(G, nodes):
    middles = find_middle(G, nodes).items()
    min_weight = min(middles, key=lambda x: x[1])[1]
    return [key for key, weight in middles if weight == min_weight]


def find_middle_one(G, nodes):
    return min(find_middle(G, nodes).items(), key=lambda x: x[1])[0]

    