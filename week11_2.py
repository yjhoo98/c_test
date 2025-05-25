import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

N = int(input().strip())
planets = []

for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((i, x, y, z))

edges = []

for dim in range(1, 4):  # 1:x, 2:y, 3:z
    planets.sort(key=lambda p: p[dim])
    for i in range(N - 1):
        a, b = planets[i], planets[i + 1]
        cost = abs(a[dim] - b[dim])
        edges.append((cost, a[0], b[0]))

edges.sort()
parent = list(range(N))
total = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost

print(total)
