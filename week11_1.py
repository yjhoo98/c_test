from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    last_year = list(map(int, input().split()))
    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)

    for i in range(n):
        for j in range(i+1, n):
            higher = last_year[i]
            lower = last_year[j]
            graph[higher][lower] = True
            indegree[lower] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) > 1:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(" ".join(map(str, result)))