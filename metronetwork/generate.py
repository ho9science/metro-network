import metronetwork as mn
import json


def generate_edge():
    temp_line = "01호선"
    prev_fr = ""
    lines = []
    edges = {}
    line_info = mn.dataloader.read_seoul_metro()
    for index, row in line_info.iterrows():
        now_line = row['호선']
        now_fr = row['외부코드']
        if prev_fr != "":
            if now_line != temp_line:
                edges[temp_line] = lines
                lines = []
                temp_line = now_line
                prev_fr = now_fr
                continue
            lines = connect_line(lines, prev_fr, now_fr)
        if prev_fr == "I138" and now_fr == "I139":
            edges[now_line] = lines
        temp_line = now_line
        prev_fr = now_fr
    add_eungam_circular(edges)
    stations = line_info.set_index('외부코드').T.to_dict('list')
    with open(mn.metro_utils.data_path("edge_list.json"), "w", encoding="utf-8") as f:
        json.dump(edges, f, indent = 4, ensure_ascii = False)
    with open(mn.metro_utils.data_path("station_list.json"), "w", encoding="utf-8") as f:
        json.dump(stations, f, indent = 4, ensure_ascii = False)
    return edges

def connect_line(lines, prev_fr, now_fr):
    if prev_fr == "161" and now_fr == "P142":
        lines.append(("141", "P142"))
        lines.append(("P142", "141"))
        return lines
    if prev_fr == "P144-1" and now_fr == "P145":
        lines.append(("P144", "P145"))
        lines.append(("P145", "P144"))
        return lines
    if prev_fr == "P157-1" and now_fr == "P158":
        lines.append(("P157", "P158"))
        lines.append(("P158", "P157"))        
        return lines
    if prev_fr == "211-4" and now_fr == "212":
        lines.append(("211", "212"))
        lines.append(("212", "211"))
        return lines
    if prev_fr == "234-4" and now_fr == "235":
        lines.append(("234", "235"))
        lines.append(("235", "234"))
        return lines
    if prev_fr == "242" and now_fr == "243":
        lines.append(("243", "201"))
        lines.append(("201", "243"))
    if prev_fr == "553" and now_fr == "P549":
        lines.append(("548", "P549"))
        lines.append(("P549", "548"))
        return lines
    if prev_fr == "610" and now_fr == "611":
        return lines
    if prev_fr == "611" and now_fr == "612":
        return lines
    if prev_fr == "612" and now_fr == "613":
        return lines
    if prev_fr == "613" and now_fr == "614":
        return lines
    if prev_fr == "614" and now_fr == "615":
        return lines
    if prev_fr == "615" and now_fr == "616":
        lines.append(("610", "616"))
        lines.append(("616", "610"))
        return lines
    if prev_fr == "K336" and now_fr == "K826":
        lines.append(("K110", "K826"))
        lines.append(("K826", "K110"))
        lines.append(("K826", "K312"))
        lines.append(("K312", "K826"))
        return lines
    if prev_fr == "K138" and now_fr == "K312":
        return lines
    if prev_fr == "K826" and now_fr == "P312":
        lines.append(("K315", "P312"))
        lines.append(("K312", "K315"))
        return lines
    if prev_fr == "702" and now_fr == "841":
        lines.append(("701", "850"))
        lines.append(("850", "701"))
        return lines
    lines.append((prev_fr, now_fr))
    lines.append((now_fr, prev_fr))
    return lines

def add_eungam_circular(edges):
    lines = [
        ("610", "611"),
        ("611", "612"),
        ("612", "613"),
        ("613", "614"),
        ("614", "615"),
        ("615", "610"),
        ]
    edges['응암순환선'] = lines
    return edges
    
def generate_transfer():
    data = mn.dataloader.read_seoul_metro()
    duplicated = data[data.duplicated(['전철역명'], keep=False)]
    test = duplicated.groupby(['전철역명'])['외부코드'].apply(list)
    out = test.to_dict()
    out["신촌"] = []
    with open(mn.metro_utils.data_path("transfer_list.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent = 4, ensure_ascii = False)

generate_edge()