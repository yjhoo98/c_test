import sys
input = sys.stdin.readline

T = int(input())
INF = int(1e9)

for _ in range(T):
    n, m = map(int, input().split())
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)  # 양방향

    k = int(input())
    friends = list(map(int, input().split()))

    for k_ in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k_] + dist[k_][j]:
                    dist[i][j] = dist[i][k_] + dist[k_][j]

    answer = 0
    min_sum = INF

    for room in range(1, n + 1):
        total = sum(dist[friend][room] for friend in friends)
        if total < min_sum:
            min_sum = total
            answer = room

    print(answer)
