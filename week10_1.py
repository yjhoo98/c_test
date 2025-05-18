import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')

dist = [[INF] * (n + 1) for _ in range(n + 1)]
path = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = k

def find_path(i, j):
    if path[i][j] == 0:
        return [i, j]
    k = path[i][j]
    return find_path(i, k)[:-1] + find_path(k, j)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            route = find_path(i, j)
            print(len(route), *route)