from metronetwork import Seoul
import metronetwork as mn
import json
import os
import networkx as nx


edgedata = os.path.join(os.path.abspath("metronetwork"), 'data', "edge_list.json")
transferdata = os.path.join(os.path.abspath("metronetwork"), 'data', "transfer_list.json")
stationdata = os.path.join(os.path.abspath("metronetwork"), 'data', "station_list.json")

def generate_edge():
    temp_line = "01호선"
    prev_fr = ""
    lines = []
    test = {}
    line_info = mn.dataloader.read_seoul_subway()
    for index, row in line_info.iterrows():
        now_line = row['호선']
        now_fr = row['외부코드']
        if prev_fr != "":
            if now_line != temp_line:
                test[temp_line] = lines
                lines = []
                temp_line = now_line
                prev_fr = now_fr
                continue
            lines = connect_line(lines, prev_fr, now_fr)

        temp_line = now_line
        prev_fr = now_fr
    stations = line_info.set_index('외부코드').T.to_dict('list')
    with open(edgedata, "w", encoding="utf-8") as f:
        json.dump(test, f, indent = 4, ensure_ascii = False)
    with open(stationdata, "w", encoding="utf-8") as f:
        json.dump(stations, f, indent = 4, ensure_ascii = False)
    return test

def connect_line(lines, prev_fr, now_fr):
    if prev_fr == "161" and now_fr == "P142":
        lines.append(("141", "P142"))
        return lines
    if prev_fr == "P144-1" and now_fr == "P145":
        lines.append(("P144", "P145"))
        return lines
    if prev_fr == "P157-1" and now_fr == "P158":
        lines.append(("P157", "P158"))
        return lines
    if prev_fr == "211-4" and now_fr == "212":
        lines.append(("211", "212"))
        return lines
    if prev_fr == "234-4" and now_fr == "235":
        lines.append(("234", "235"))
        return lines
    if prev_fr == "242" and now_fr == "243":
        lines.append(("243", "201"))
    if prev_fr == "553" and now_fr == "P549":
        lines.append(("548", "P549"))
        return lines
    if prev_fr == "615" and now_fr == "616":
        lines.append(("610", "616"))
        return lines
    if prev_fr == "K336" and now_fr == "K826":
        lines.append(("K110", "K826"))
        lines.append(("K826", "K312"))
        return lines
    if prev_fr == "K138" and now_fr == "K312":
        return lines
    if prev_fr == "K826" and now_fr == "P312":
        lines.append(("K315", "P312"))
        return lines
    if prev_fr == "702" and now_fr == "841":
        lines.append(("701", "850"))
        return lines
    lines.append((prev_fr, now_fr))
    return lines
    
def generate_transfer():
    data = mn.dataloader.read_seoul_subway()
    duplicated = data[data.duplicated(['전철역명'], keep=False)]
    test = duplicated.groupby(['전철역명'])['외부코드'].apply(list)
    out = test.to_dict()
    with open(transferdata, "w", encoding="utf-8") as f:
        json.dump(out, f, indent = 4, ensure_ascii = False)
