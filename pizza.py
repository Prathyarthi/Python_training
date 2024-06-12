def solve(n,y):
    for i in range(y,n+1):
        if n%i == 0:
            return sum(int(x) for x in str(i))
    return -1

n,y = list(map(int,input().split()))
print(solve(100,17))


