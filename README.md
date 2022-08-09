# metro-network

[![Build Status](https://travis-ci.org/ho9science/subway-line-graph.png?branch=master)](https://travis-ci.org/ho9science/subway-line-graph)

metro-network is a python library for making graph model of subway line map using open data.

metro-network는 공공데이터 포털에서 제공하는 지하철 노선 정보를 활용해 만든 그래프 모델을 만들 수 있는 파이썬 라이브러리입니다.

### dataset
> 데이터 셋은 서울시 공공데이터를 기반으로 가공하여 사용합니다.

* [서울특별시 노선별 지하철역 정보](http://data.seoul.go.kr/dataList/OA-15442/S/1/datasetView.do)



### 중간 지점 찾기

> 세 출발지점이 균등한 중간 지점을 찾습니다.
```
import networkx as nx
import metronetwork as mn

seoul = mn.Seoul()
G = seoul.make_seoul_metro_network()

departure_a = seoul.station("석남")
route_b = seoul.station("동대문")
route_c = seoul.station("마천")

result = mn.find_center_one(G, [route_a, route_b, route_c])
result = mn.find_center_top5(G, [route_a, route_b, route_c])
```

### 중간 지점 찾기

> 세 출발지점의 최소 거리의 합인 중간 지점을 찾습니다.
```
import networkx as nx
import metronetwork as mn

seoul = mn.Seoul()
G = seoul.make_seoul_metro_network()

route_a = seoul.station("석남")
route_b = seoul.station("동대문")
route_c = seoul.station("마천")

result = mn.find_middle_one(G, [route_a, route_b, route_c])
result = mn.find_middle_sort(G, [route_a, route_b, route_c])

```
### 길찾기 example
```
import networkx as nx
import metronetwork as mn

seoul = mn.Seoul()
G = seoul.make_seoul_metro_network()

length, path = nx.bidirectional_dijkstra(G, '135', '132')
path = nx.shortest_path(G, "414", "237")
```