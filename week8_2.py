def is_possible(lectures, m, capacity):
    count = 1
    total = 0

    for time in lectures:
        if total + time > capacity:
            count += 1
            total = time
        else:
            total += time

    return count <= m

def b_s(lectures, m):
    left = max(lectures)
    right = sum(lectures)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if is_possible(lectures, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

N,M=map(int,input().split())

lecture=list(map(int, input().split()))

print(b_s(lecture, M))