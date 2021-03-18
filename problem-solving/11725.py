import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]


for _ in range(node - 1):
    i, j = map(int, input().split())
    node_graph[i].append(j)
    node_graph[j].append(i)


def dfs(graph_list, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent


for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])
