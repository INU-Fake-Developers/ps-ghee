import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

dic = {}
for i in range(int(input())):               # 첫째 줄에는 컴퓨터의 수가 주어진다
    dic[i+1] = set()
for j in range(int(input())):               # 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다
    a, b = map(int, input().split())        # 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
    dic[a].add(b)
    dic[b].add(a)


def dfs(start, dic):                        # bfs 로도 가능하며 차이는 유사하다. bfs 와 dfs 성능이 비슷할 경우, 보통 dfs 를 선호한다.
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


visited = []
dfs(1, dic)
print(len(visited)-1)
