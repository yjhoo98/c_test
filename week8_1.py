import bisect

def lis(arr):
    result = []
    for num in arr:
        idx = bisect.bisect_left(result, num)
        if idx == len(result):
            result.append(num)
        else:
            result[idx] = num
    return len(result)
N=int(input())
series=list(map(int, input().split()))
print(f'{lis(series)}')

