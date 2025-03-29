def num_people(k,n):

    fl = [[0] * (n+1) for _ in range(k + 1)]
    for i in range(1,n+1):
        fl[0][i]=i


    for i in range(1,k+1):
        for j in range(1,n+1):
           fl[i][j]=fl[i][j-1]+fl[i-1][j]
    return fl[k][n]

t=int(input())
k=list()
n=list()
for i in range(t):
    k.append(int(input()))
    n.append(int(input()))

for i in range(t):
    print(num_people(k[i],n[i]))