from collections import deque


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
c_room = [list(input().strip()) for _ in range(n)]


x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0 #점프 횟수

while True:
    count += 1 #점프 횟수 증가
    visited = [[False] * m for _ in range(n)] #방문 기록에 대한 2차원 리스트 생성
    q = deque()
    q.append((x1, y1))
    visited[x1][y1] = True #주난의 시작점에서 시작하므로 True로 변경

    found = False  # 범인 발견 여부(처음엔 발견 못했으므로 False)

    while q:
        x, y = q.popleft() #초기엔 q[(x1,y1)]이므로 x=x1,y=y1이 된다.

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # n*m 2차원 리스트를 벗어나지 않고 방문기록이 없을 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True

                if c_room[nx][ny] == '0':
                    q.append((nx, ny)) #장애물 없는 경우
                elif c_room[nx][ny] == '#':
                    found = True #범인을 발견했으므로 발견 여부가 True가 되고 for문 종료
                    break
                elif c_room[nx][ny] == '1':
                    c_room[nx][ny] = '0'  # 장애물이 있는 경우 (다음 턴부터 이동 가능)

        if found:    # found=True일 때 while q: 종료
            break

    if found:    #found=True 일 때 count출력하고 무한루프 종료
        print(count)
        break