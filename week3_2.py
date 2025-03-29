import sys
n,m=map(int,sys.stdin.readline().split())# n:바구니 개수/m: 공 넣는 횟수

buckets=[0 for _ in range(n)]
for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split())  # i~j번 바구니까지 k번 공을 넣음
    for t in range(i-1,j):
        buckets[t]=k
for s in range(len(buckets)):
    print(buckets[s],end=' ')