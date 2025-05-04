def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def len_series(n):
    result=[]

    if is_prime(n):
        return 0
    else:
        start=n
        end=n
        while not is_prime(start):
            start-=1
        while not is_prime(end):
            end+=1
        for i in range(start,end):

            result.append(i)
    return len(result)
T=int(input())
arr=[]
for _ in range(T):
    k=int(input())
    arr.append(k)
for i in range(T):
    print(f'{len_series(arr[i])}')