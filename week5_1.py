import sys
N=int(sys.stdin.readline())
dots=[[0,0] for _ in range(N)]

for i in range(N):
    M,K=map(int,input().split())
    dots[i][0]=M
    dots[i][1]=K

dots.sort()

for i in range(N):
    print(f'{dots[i][0]} {dots[i][1]}')