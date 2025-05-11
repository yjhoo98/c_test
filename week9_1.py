from collections import deque

N = int(input())
A, B, C = map(int, input().split())
x = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(S[-1] + x[i])
print(S)
dp = [0]*(N+1)

def cross_p(f, g):
    return (g[1] - f[1])/(f[0] - g[0])

stack = deque([[0, 0, 0]])

for i in range(1, N+1):
    X = S[i]
    while len(stack) >= 2 and stack[1][2] < X:
        stack.popleft()

    stack_index = 0
    dp[i] = X * stack[stack_index][0] + stack[stack_index][1] + A * X ** 2 + B * X + C

    f = [-2 * A * S[i], A * S[i] ** 2 - B * S[i] + dp[i], 0]
    tmp = cross_p(f, stack[-1])
    f[2] = tmp
    stack.append(f)

    while len(stack) >= 3 and cross_p(stack[-3], stack[-2]) > cross_p(stack[-2], stack[-1]):
        tmp = stack.pop()
        stack.pop()
        stack.append(tmp)
    stack[-1][2] = cross_p(stack[-1], stack[-2])

print(dp[-1])