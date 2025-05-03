from collections import deque

n,c=map(int,input().split())
t=list()
a=list()
b=list()
for _ in range(c):
    ti, ai, bi = map(int, input().split())
    t.append(ti)
    a.append(ai)
    b.append(bi)

portal = dict()
for i in range(c):
    portal[a[i]] = (t[i], b[i])

distance = [float('inf')] * n
distance[0] = 0

dq = deque()
dq.append(0)

while dq:
    current = dq.popleft()

    if current == n - 1:
        break

    if current in portal:
        p_type, goal = portal[current]
        if distance[goal] > distance[current]:
            distance[goal] = distance[current]
            dq.appendleft(goal)

        if p_type == 1 and current + 1 < n:
            if distance[current + 1] > distance[current] + 1:
                distance[current + 1] = distance[current] + 1
                dq.append(current + 1)

    else:
        if current + 1 < n and distance[current + 1] > distance[current] + 1:
            distance[current + 1] = distance[current] + 1
            dq.append(current + 1)

print(distance[n - 1] if distance[n - 1] != float('inf') else -1)