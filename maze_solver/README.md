# Astar Algorithm
최단경로 미로찾기 프로젝트 : 장애물이 있는 M∗N 크기의 maze 내에서 설정된 START점부터 GOAL점까지의 최단경로 탐색

<p align='center'><img src="images/processing_result.png" width="500"></p>

## 1. Data Structure
### 1.1 class `Node`
- maze의 각 점(칸)이 되는 객체
- START 노드에서부터 GOAL 노드에 도달할 때까지 이동하며 경로를 탐색하는 주체이다.





#### 1.1.1 variables
```
F = G + H
G : 지금까지 온 경로 길이
H : 앞으로 갈 경로 길이
```

**(1) G**
- START 노드에서부터 현재 노드까지의 경로 거리
- 대각선 경로 포함
- 계산 : (부모노드의 G값) + (10 or 14)
- 부모노드의 동/서/남/북 방향의 노드인 경우 부모노드로부터 자식노드의 경로를 10으로 설정
- 부모노드의 북동/북서/남동/남서 방향의 노드인 경우 부모노드로부터 자식노드의 경로를 14로 설정 (2‾√배)
- data type : `int`



**(2) H**
- 현재 노드에서부터 GOAL까지의 경로 거리
- 대각선 경로 불포함
- 계산 : [{(GOAL의 x 좌표) - (현재노드의 x 좌표)} + {(GOAL의 y 좌표) - (현재노드의 y 좌표)}] * 10
- daya type : `int`



**(3) F**



**(4) location**
- 각 노드의 좌표
- 미로 맵의 가장 왼쪽 아래 점이 (0, 0)으로, x축과 y축에 따라 오른쪽, 위쪽을 양의 방향으로 증가한다.
- daya type : `tuple`



**(4) parent**
- 부모노드의 좌표
- 현재 노드의 G값 계산 시에 parent의 G값을 이용하여 계산할 수 있다.
- START로부터 현재 노드까지의 경로는 현재 노드에서부터 START까지 연결된 parent들의 집합이다.
- data type : `tuple`











### 1.2 class `Astar`
- 주어진 maze에 대한 최단경로를 탐색하는 객체
- maze, maze의 모든 노드, 경로를 탐색하며 쌓이는 객체들의 리스트 등 maze에 대한 모든 정보를 저장하며 경로를 탐색한다.


#### 1.2.1 variables


**(1) maze_map**
- user로부터 input으로 받은 maze의 지도로, 2차원 형태의 list
- 가공되지 않은 형태의 maze map
- list의 모든 요소는 0 또는 1로 이루어져 있다.
  - `0` : barrier가 아닌 칸. START나 GOAL 노드가 될 수 있다.
  - `1` : barrier인 칸. START나 GOAL 노드는 barrier인 칸에 설정할 수 없다.
- Astar 클래스의 내장함수 encode_map을 이용해 maze_dict로 변환된다.
- data type : `list`



**(2) maze_dict**
- maze_map을 encoding하여 모든 점(칸)을 노드 객체로써 저장한 딕셔너리
  - `key` : 노드의 location(좌표)
  - `value` : 노드 객체
- maze의 모든 노드를 저장하며, 현재 노드의 주변 노드를 탐색, 탐색된 노드를 리스트에 저장할 때 maze_dict의 정보를 불러와서 쓰게 된다.
- data type : dic
- key data type : `tuple`
- value data tupe : `Node instance`



**(3) START, GOAL**
- START점과 GOAL점의 노드
- 주어진 maze에서 start점과 goal점을 Node객체로써 저장한다.
- data type : `Node instance`



**(4) barrier_list**
- maze_map에서 설정된 barrier의 좌표가 저장된 list
- maze_map을 maze_dict로 encoding할 때 barrier인 칸들의 좌표를 저장한다.
- data type : `list`



**(5) opened_list**
- 현재까지 search 된 모든 노드 좌표가 저장된 list
- 새로운 노드들을 search할 때 barrier_list, closed_list에 있는 좌표는 제외된다.
- data type : `list`



**(6) closed_list**
- 현재까지 search 된 노드 중, 경로로써 선택된 노드의 좌표가 저장된 list
- 경로를 탐색하는 과정에서 G, H, F값의 비교를 통해 적절히 노드를 선택해 경로를 쌓을 때 경로가 되는 노드를 저장한다.
- data type : `list`



**(7) DIR**
- 8가지 방향 (동/서/남/북/남동/남서/북동/북서) 의 좌표와 그에 따른 경로길이 (10 or 14)를 저장한 상수 변수
- 딕셔너리 형태로써 key에는 8방향의 튜플을, value에는 10 또는 14의 경로 길이를 저장한다.
  - `key` : 8방향 (-1, 1), (0, +1), (+1, +1), (+1, 0), (+1, -1), (+1, -1), (0, -1), (-1, -1), (-1, 0)
  - `value` : 10 or 14
- data type : `dict`
- key data type : `tuple`
- value data type : `int`











### 1.2.2 functions
